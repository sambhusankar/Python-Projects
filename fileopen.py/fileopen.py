try:

    f1=open('text.txt','r')
    data=f1.read()
    print(data)
    
except Exception as e:
    print(e)
    
    
finally:
    try:
        f1=open('poem.tx','r')
        data=f1.read()
        print(data)
    
    except Exception as e:
        print(e)
        