import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import sys
import os

class GradeAnalyzer:
    def __init__(self, input_file):
        self.df = pd.read_excel(input_file)
        self.check_columns()
        
    def check_columns(self):
        required = ['ФИО', 'Оценка']
        if not all(col in self.df.columns for col in required):
            raise ValueError(f"Нужны колонки: {required}")

    def analyze(self):
        stats = {
            'Средний балл': round(self.df['Оценка'].mean(), 2),
            'Медиана': self.df['Оценка'].median(),
            'Максимум': self.df['Оценка'].max(),
            'Минимум': self.df['Оценка'].min(),
            'Количество': len(self.df)
        }
        return stats
    
    def plot_grades(self, filename='grades_chart.png'):
        plt.figure(figsize=(10, 6))
        self.df.plot(kind='bar', x='ФИО', y='Оценка', legend=False)
        plt.title('Успеваемость класса')
        plt.ylabel('Баллы')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        return filename
    
    def generate_report(self, output_file):
        stats = self.analyze()
        chart_file = self.plot_grades()
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Отчет по успеваемости', 0, 1, 'C')
        pdf.set_font('Arial', '', 12)
        
        pdf.ln(10)
        for key, value in stats.items():
            pdf.cell(0, 10, f'{key}: {value}', 0, 1)
            
        pdf.ln(10)
        pdf.image(chart_file, x=10, w=190)
        
        pdf.output(output_file)
        os.remove(chart_file)  # Удаляем временный файл
        return output_file

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python grades_analyzer.py входной_файл.xlsx выходной_файл.pdf")
    else:
        try:
            analyzer = GradeAnalyzer(sys.argv[1])
            report_file = analyzer.generate_report(sys.argv[2])
            print(f"Отчет сохранен: {report_file}")
        except Exception as e:
            print(f"Ошибка: {str(e)}")
