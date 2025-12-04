dictionary = {}
print("請輸入英漢辭典，當英文內容輸入123時結束：")

while True:
  key = input("英文：")
  if key == "123":
    break
  elif key.isalpha() != True:
    print("請輸入英文單字")
    continue
  elif dictionary.get(key.lower(), "none") != "none":
    print("此單字已建檔，請勿重複建檔")
    continue

  value = input("中文：")
  dictionary[key.lower()] = value

print("*********************")
while True:
  word = input("請輸入想查詢的單字，內容輸入123時結束：")
  if word == "123":
    break
  result = dictionary.get(word.lower(), "單字不存在")
  print(result)