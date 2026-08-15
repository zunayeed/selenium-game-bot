from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS?ref_=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_cav_p_1_0&pd_rd_i=B01NBKTPTS&pd_rd_w=Icacb&content-id=amzn1.sym.4a6480f2-00b3-4e33-a59d-ae768449426b&pf_rd_p=4a6480f2-00b3-4e33-a59d-ae768449426b&pf_rd_r=QHTE1C3PM9HXBJSA2SG4&pd_rd_wg=9hH1M&pd_rd_r=5bcf933c-b75d-45d0-aad4-035844433e4c&th=1")
driver.get("https://www.python.org/")
#price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

#print(f"The price is {price_dollar.text}.{price_cents.text}")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))


driver.quit()