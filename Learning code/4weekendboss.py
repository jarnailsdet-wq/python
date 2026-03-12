#weekend boss
Failed_testes=[]
for i in range(1,6):
    print(f"Running Test {i}")
    result=input("Enter test result Pass or fail : ").lower()
    if result=="fail":
        Failed_testes.append(i)
print(f"Failed tests : {Failed_testes}")