import os
import re
import pandas as pd

# Projelerin bulunduğu dizin
BASE_DIR = '.'

# Sayılacak dosya uzantıları ve ilişkili teknolojiler
FILE_EXTENSIONS = {
    '.java': 'Java',
    '.xml': 'Android XML',
    '.gradle': 'Gradle',
    '.kt': 'Kotlin',
    '.aar': 'Android Archive',
    '.swift': 'Swift',
    '.m': 'Objective-C',
    '.xib': 'Interface Builder',
    '.storyboard': 'Storyboard',
    '.html': 'HTML',
    '.css': 'CSS',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.py': 'Python',
    '.c': 'C',
    '.cpp': 'C++',
    '.h': 'C/C++ Header',
    '.cs': 'C#',
    '.go': 'Go',
    '.rb': 'Ruby',
    '.php': 'PHP',
    '.dart': 'Dart',
    '.sql': 'SQL',
    '.sh': 'Shell Script',
    '.bat': 'Batch Script',
    '.pl': 'Perl',
    '.r': 'R',
    '.scala': 'Scala',
    '.json': 'JSON',
    '.yaml': 'YAML',
    '.yml': 'YML',
    '.txt': 'Text File',
    '.md': 'Markdown',
    '.dockerfile': 'Dockerfile',
    '.jsp': 'Java Server Pages',
    '.vb': 'Visual Basic',
}

# Yorum satırlarını belirlemek için desenler
COMMENT_PATTERNS = {
    '.py': r'^\s*#',  # Python
    '.java': r'^\s*//|/\*.*\*/',  # Java
    '.c': r'^\s*//|/\*.*\*/',  # C/C++
    '.cpp': r'^\s*//|/\*.*\*/',  # C++
    '.js': r'^\s*//',  # JavaScript
    '.rb': r'^\s*#',  # Ruby
    '.php': r'^\s*//|/\*.*\*/',  # PHP
    '.swift': r'^\s*//',  # Swift
    # Daha fazla dil için desen eklenebilir
}

# Satır sayısını bulma fonksiyonu
def count_lines_in_file(file_path):
    lines_count = 0
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            # Yorum satırı kontrolü
            is_comment = False
            ext = os.path.splitext(file_path)[1]  # Dosya uzantısını al
            if ext in COMMENT_PATTERNS:
                # Eğer satır, yorum satırı ise, sayma
                if re.match(COMMENT_PATTERNS[ext], line):
                    is_comment = True

            # Eğer yorum değilse ve satır boş değilse, say
            if not is_comment and line.strip():
                lines_count += 1

    return lines_count

# Projelerin toplam satır sayısını ve kullanılan teknolojileri hesaplama
def count_lines_in_projects(base_dir):
    project_data = []
    total_lines = 0
    project_index = 1

    for project_name in os.listdir(base_dir):
        project_path = os.path.join(base_dir, project_name)
        if os.path.isdir(project_path):  # Sadece dizinleri kontrol et
            project_lines = 0
            technologies = set()  # Teknoloji bilgilerini saklamak için set

            for root, _, files in os.walk(project_path):
                for file in files:
                    ext = os.path.splitext(file)[1]  # Dosya uzantısını al
                    if ext in FILE_EXTENSIONS:
                        file_path = os.path.join(root, file)
                        project_lines += count_lines_in_file(file_path)
                        technologies.add(FILE_EXTENSIONS[ext])  # Kullanılan teknolojiyi ekle

            project_data.append({
                'S.No': project_index,
                'Project name': project_name,
                'Lines of code': project_lines,
                'Technologies': ', '.join(technologies)  # Teknolojileri virgülle ayır
            })
            if project_lines == 0:
                print(f'Warning: No lines found in project "{project_name}".')
            total_lines += project_lines
            project_index += 1

    return project_data, total_lines


def main():
    project_data, total_lines = count_lines_in_projects(BASE_DIR)

    # Pandas DataFrame ile tablo oluştur
    df = pd.DataFrame(project_data)

    # Excel dosyasına yaz
    output_file = 'project_lines_summary.xlsx'
    df.to_excel(output_file, index=False)

    print(f"Excel dosyası '{output_file}' olarak kaydedildi.")
    print(f"TOPLAM : {total_lines:,}")  # Toplam satır sayısını yazdır

if __name__ == '__main__':
    main()
