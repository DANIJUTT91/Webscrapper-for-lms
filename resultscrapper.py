from selenium.webdriver.common.by import By
from selenium import webdriver 
import pandas as pd

df = pd.read_excel('students.xlsx')
names = df['Names']
ag_NOs = df['Ag']

driver = webdriver.Chrome() 
# driver.get("http://lms.uaf.edu.pk/login/index.php") 

for ag, name in zip(ag_NOs, names):
    driver.get("http://lms.uaf.edu.pk/login/index.php") 
    input_text_fname = driver.find_element(By.ID, 'REG')
    input_text_fname.send_keys(ag)
    button = driver.find_element(By.CLASS_NAME, "btn-warning")
    button.click()
    page = driver.page_source
    lines = page.split("\n")

    subject = 'IT-503'
    subject_line_number = None
    for i, item in enumerate(lines):
        if subject in item:
            subject_line_number = i
            break
    if subject_line_number != None:
        one_result = 'Marks: '+lines[subject_line_number+7][-7]+ lines[subject_line_number+7][-6] + '\n' + 'Grade: '+lines[subject_line_number+8][-6]

    print(one_result)
    try:
        output = r'E:\Study\general\Python\results.txt'
        with open(output, 'a') as f:
            f.write('\n\n'+'AG: '+ag+' ' + '\nName: ' + str(name)+'\n'+one_result)
        print("File 'results.txt' written successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    