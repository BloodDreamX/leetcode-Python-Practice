# 維基百科https://zh.wikipedia.org/zh-tw/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97

def roman_to_arabic(roman):
    # 定義羅馬數字和對應的阿拉伯數字
    #建立字典功能
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    arabic = 0
    prev_value = 0
    
    # 從右到左處理羅馬數字(ChatGPT)
    #用迴圈的方式，把一個一個字元讀取進來(從右邊到左邊)
    for char in reversed(roman):
        value = roman_dict[char]
        
        
        # 如果當前數字小於前一個數字，則需要減去當前數字
        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        
        prev_value = value
    #print(prev_value)
    return arabic

# 轉換
roman_number = input("請輸入羅馬數字：")
arabic_number = roman_to_arabic(roman_number)
print(f"羅馬數字 {roman_number} 轉換為阿拉伯數字是 {arabic_number}")
