import pandas as pd

def main():
    _data ={
        'id': [0,1,2,3],
        'people': ['kim', 'steven', 'max', 'willa'],
        'role': ['DE', 'DS', 'DE', 'EM']
    }
    df =pd.DataFrame(_data)
    breakpoint()

    df.to_csv('output.csv', index = False)

if __name__=='__main__':
    main()