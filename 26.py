nums = []#建立一個List ，允許重複值
nums = input("請輸入數字，以空白分隔：").split()#將數列切割，會儲存成str類型list
myset = set(nums)#將list轉換為set，用來移除重複值
nums = list(myset)#將內容從set倒回去List裡面
nums.sort()#將list進行排序
print(f"{len(nums)}, nums = {nums}")#輸出移除重複值後的list數量、內容