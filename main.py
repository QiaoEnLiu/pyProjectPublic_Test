# main.py
# Step 1：main.py先讀取shared_module.py的global_variable
# Step 2：main.py叫sub.py修改shared_module.py的global_variable
    # Step 2.1：sub.py對shared_module.py的global_variable進行修改
# Step 3：然後main.py再讀取shared_module.py的global_variable

# 匯入共享模組
import shared_module
from sub import modify_global_variable

def main():
    # 在函數內部使用全域變數
    print("Step 1 ", shared_module.global_variable)

    print("Step 2 Modify")
    # 呼叫 sub.py 中的函數修改 global_variable
    modify_global_variable()

    # 再次印出修改後的 global_variable
    print("Step 3：", shared_module.global_variable)

# 如果需要在 main.py 中執行一些程式碼，可以放在這裡
if __name__ == "__main__":
    main()