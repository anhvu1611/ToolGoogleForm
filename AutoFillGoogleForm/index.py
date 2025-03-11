from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import random

# Đường dẫn đến ChromeDriver
driver_path = r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

for _ in range(20):
    driver = webdriver.Chrome(service=service)

    # URL Google Form
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLScGkuz1xXGceMckj_c9JlTkqxYeX__yh5Gq_Rf3doKcCc1Byg/viewform"
    driver.get(form_url)

    gender_choices = ["Nam", "Nữ"]
    selected_gender = random.choice(gender_choices)

    age_choices = ["Từ 18-25 tuổi", "Từ 25-35 tuổi"]
    selected_age = random.choice(age_choices)

    nghenghiep = ["Sinh Viên", "Khác", "Kĩ Thuật và Công Nghệ", "Kinh Doanh"]
    chonnghe = random.choice(nghenghiep)

    thunhap = ["Dưới 10 triệu", "Từ 10 triệu đến 20 triệu", "Từ 20 triệu đến 30 triệu", "Trên 30 triệu"]
    chonthunhap = random.choice(thunhap)

    tungmua = ["1 lần", "2 đến 3 lần", "3 đến 5 lần", "Trên 5 lần"]
    chontungmua = random.choice(tungmua)

    tuoitho = ["Dưới 1 năm", "Từ 1 đến 2 năm", "Từ 2 đến 3 năm", "Trên 3 năm"]
    chontuoitho = random.choice(tuoitho)

    thuonghieu = ["Apple", "Samsung", "Xiaomi", "Oppo"]
    chonthuonghieu = random.choice(thuonghieu)

    phan2 = ["5", "4", "3"]
    chonphan2 = random.choice(phan2)

    phan3 = ["5", "4", "3"]
    chonphan3 = random.choice(phan3)

    phan4 = ["5", "4", "3"]
    chonphan4 = random.choice(phan4)

    phan5 = ["5", "4", "3"]
    chonphan5 = random.choice(phan5)

    phan6 = ["5", "4", "3"]
    chonphan6 = random.choice(phan6)

    phan7 = ["5", "4", "3"]
    chonphan7 = random.choice(phan7)

    phan8 = ["5", "4", "3"]
    chonphan8 = random.choice(phan8)
    

    try:
        # Chờ form tải xong
        wait = WebDriverWait(driver, 10)

        # --- PHẦN 1 ---
        # Câu 1: "Đã từng"
        question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]'))
        )
        question_1.click()

        # Câu 2: "Có"
        question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]'))
        )
        question_2.click()

        
        # Câu 3: "Nam"
        question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//div[@role="radio" and @aria-label="{selected_gender}"]'))
        )
        question_3.click()

        # Câu 4: "Từ 18-25 tuổi"
        question_4 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//div[@role="radio" and @aria-label="{selected_age}"]'))
        )
        question_4.click()

        # Câu 5: "Sinh Viên"
        question_5 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//div[@role="radio" and @aria-label="{chonnghe}"]'))
        )
        question_5.click()

        # Câu 6: "Dưới 10 triệu"
        question_6 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//div[@role="radio" and @aria-label="{chonthunhap}"]'))
        )
        question_6.click()

        # Câu 7: "Có"
        question_7 = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="radio" and @aria-label="Có"]'))
        )
        question_7.click()

        # Câu 8: "1 lần"
        question_8 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//div[@role="radio" and @aria-label="{chontungmua}"]'))
        )
        question_8.click()

        # Câu 9: "Dưới 1 năm"
        question_9 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//div[@role="radio" and @aria-label="{chontuoitho}"]'))
        )
        question_9.click()

        # Câu 10: "Apple"
        question_10 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//div[@role="radio" and @aria-label="{chonthuonghieu}"]'))
        )
        question_10.click()

        # Gửi form (Trang 1)
        submit_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span'))
        )
        submit_button.click()
        print("Submitted Page 1!")

        # --- CHỜ TRANG 2 ---
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div'))
        )
        print("Loaded Page 2!")

        # --- PHẦN 2 ---
        # Ví dụ chọn mức "5" cho tất cả câu hỏi
        # Định vị tất cả các đáp án mức "5"
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # --- GIÁ CẢ (GC) ---
        gc_question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[{chonphan2}]/div/div/div[3]/div'))  # Thay "1" bằng câu trả lời bạn muốn
        )

        gc_question_1.click()

        gc_question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[{chonphan3}]/div/div/div[3]/div'))  # Thay "2" bằng câu trả lời bạn muốn
        )
        gc_question_2.click()

        gc_question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[{chonphan4}]/div/div/div[3]/div'))
        )
        gc_question_3.click()

        tn_question_4 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[{chonphan5}]/div/div/div[3]/div'))
        )
        tn_question_4.click()


        #Tính năng sản phẩm (TN)
        tn_question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[{chonphan6}]/div/div/div[3]/div'))
        )
        tn_question_1.click()

        xh_question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[{chonphan7}]/div/div/div[3]/div'))
        )
        xh_question_2.click()

        xh_question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[{chonphan8}]/div/div/div[3]/div'))
        )
        xh_question_3.click()

        th_question_4 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[{chonphan3}]/div/div/div[3]/div'))
        )
        th_question_4.click()

        # --- ẢNH HƯỞNG XÃ HỘI (XH) --
        tt_question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[{chonphan2}]/div/div/div[3]/div'))
        )
        tt_question_1.click()

        gt_question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[{chonphan4}]/div/div/div[3]/div'))
        )
        gt_question_2.click()

        nc_question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[{chonphan8}]/div/div/div[3]/div'))
        )
        nc_question_3.click()

        qd_question_4 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[{chonphan5}]/div/div/div[3]/div'))
        )
        qd_question_4.click()

        # --- SỰ THUẬN TIỆN  (TT) --
        th_question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[2]/span/div[{chonphan6}]/div/div/div[3]/div'))
        )
        th_question_1.click()

        gt_question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[4]/span/div[{chonphan7}]/div/div/div[3]/div'))
        )
        gt_question_2.click()

        nc_question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[6]/span/div[{chonphan3}]/div/div/div[3]/div'))
        )
        nc_question_3.click()

        qd_question_4 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[{chonphan2}]/div/div/div[3]/div'))
        )
        qd_question_4.click()

        # --- THUONG HIEU (TH) --
        th_question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[{chonphan2}]/div/div/div[3]/div'))
        )
        th_question_1.click()

        gt_question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[{chonphan4}]/div/div/div[3]/div'))
        )
        gt_question_2.click()

        nc_question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[{chonphan2}]/div/div/div[3]/div'))
        )
        nc_question_3.click()

        qd_question_4 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[{chonphan6}]/div/div/div[3]/div'))
        )
        qd_question_4.click()

        # --- GIÁ TRỊ CẢM NHẬN VÀ HẬU MÃI --
        th_question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[2]/span/div[{chonphan2}]/div/div/div[3]/div'))
        )
        th_question_1.click()

        gt_question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[4]/span/div[{chonphan7}]/div/div/div[3]/div'))
        )
        gt_question_2.click()

        nc_question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[6]/span/div[{chonphan6}]/div/div/div[3]/div'))
        )
        nc_question_3.click()

        qd_question_4 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[8]/span/div[{chonphan8}]/div/div/div[3]/div'))
        )
        qd_question_4.click()

        # --- Nhu cầu --
        th_question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[2]/span/div[{chonphan2}]/div/div/div[3]/div'))
        )
        th_question_1.click()

        gt_question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[4]/span/div[{chonphan3}]/div/div/div[3]/div'))
        )
        gt_question_2.click()

        nc_question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[6]/span/div[{chonphan5}]/div/div/div[3]/div'))
        )
        nc_question_3.click()

        qd_question_4 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[8]/span/div[{chonphan6}]/div/div/div[3]/div'))
        )
        qd_question_4.click()

        # --- Quyết định (TH) --
        th_question_1 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[{chonphan7}]/div/div/div[3]/div'))
        )
        th_question_1.click()

        gt_question_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[4]/span/div[{chonphan8}]/div/div/div[3]/div'))
        )
        gt_question_2.click()

        nc_question_3 = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[6]/span/div[{chonphan3}]/div/div/div[3]/div'))
        )
        nc_question_3.click()

        # Kiểm tra xem có nút "Tiếp" hay không và bấm vào (nếu có)
        try:
            next_button = driver.find_element(By.XPATH, '//span[text()="Tiếp"]')
            next_button.click()
            print("Đã chuyển sang trang tiếp theo trong phần 2!")
        except:
            print("Không tìm thấy nút Tiếp, tiếp tục xử lý các câu hỏi khác.")

        # Gửi form ở cuối trang 2
        submit_button_2 = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span'))
        )
        submit_button_2.click()
        print("Submitted Page 2!")

    except Exception as e:
        print(f"Lỗi xảy ra ở Phần 2: {e}")

    finally:
        driver.quit()