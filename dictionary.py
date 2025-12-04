dictionary = {}
print("請輸入英漢辭典，當key輸入end時結束：")

while True:
  key = input("Key：")
  if key == "end":
    break
  value = input("Value：")
  dictionary[key.lower()] = value

word = input("請輸入想查詢的單字：")
result = dictionary.get(word.lower(), "單字不存在")
print(result)