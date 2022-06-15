import tkinter as tk
import pandas as pd


class MyFrame(tk.LabelFrame):

    def __init__(self, root):
        tk.LabelFrame.__init__(self, root, text="資料比對工具")
        # 標籤: Label
        self.l1 = tk.Label(self, text="DATA 1:")
        self.l1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 單行輸入: Entry
        self.e1 = tk.Entry(self)
        self.e1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 按紐: Button
        self.b1 = tk.Button(self, text="選擇檔案")
        # tk.X
        self.b1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 標籤: Label
        self.l2 = tk.Label(self, text="DATA 2:")
        self.l2.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 單行輸入: Entry
        self.e2 = tk.Entry(self)
        self.e2.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 按紐: Button
        self.b2 = tk.Button(self, text="選擇檔案")
        # tk.X
        self.b2.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 標籤: Label
        self.l3 = tk.Label(self, text="輸出檔案位置:")
        self.l3.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 單行輸入: Entry
        self.e3 = tk.Entry(self)
        self.e3.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 按紐: Button
        self.b3 = tk.Button(self, text="輸出檔案位置")
        # tk.X
        self.b3.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 按紐: Button
        self.b4 = tk.Button(self, text="執行", command=self.DATA)
        # tk.X
        self.b4.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        self.result = tk.Label(self, text="按上面按鈕進行資料比對...")
        self.result.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)

    def DATA(self):
        df1 = pd.read_csv(self.e1)
        df2 = pd.read_csv(self.e2)
        pd_final = pd.merge(df1, df2, how="left", on="POLICY_NO", )
        pd_final.to_csv("DATA_FINAL.csv")

window = tk.Tk()
window.geometry("500x500+100+100")
f1 = MyFrame(window)
f1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)
window.mainloop()





