# sub.py

# 匯入共享模組
import shared_module

def modify_global_variable():
    # 在 sub.py 中修改 shared_module.py 的 global_variable
    shared_module.global_variable = 15
    print("Step 2.1：", shared_module.global_variable)
