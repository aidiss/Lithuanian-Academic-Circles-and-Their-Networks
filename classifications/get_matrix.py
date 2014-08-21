# -*- coding: utf-8 -*-

def get_matrix(df, tipas='kryptys'): #2014 07 22
    """
    Creates a matrix from pandas DataFrame object.
    
    Args:
    df - pandas dataframe object
    tipas - kind of matrix. default choice is 'kryptys' that stands for
    'diretions
    
    Returns:
    Nothing, but shows a matrix
    """
    
  #  plt.figure(figsize=(8, 10))
    sakos = df['skspvd'].unique()
    kryptys = df['krppvd'].unique()
    df2 = pd.DataFrame(index=sakos, columns=kryptys)
    
    if tipas == 'kryptys':
        for x in sakos:
            if len(df[df['skspvd'] == x].krppvd.values) > 0:
                for y in df[df['skspvd'] == x].krppvd.values:
                    df2[y][x] = True
                    
    if tipas == 'sakos':
        df2 = pd.DataFrame(index=kryptys, columns=sakos)
        for x in kryptys:
            if len(df[df['krppvd'] == x].skspvd.values) > 0:
                for y in df[df['krppvd'] == x].skspvd.values:
                    df2[y][x] = True
                

    df2.fillna(False,inplace=True)
    spearman = df2.corr(method='spearman', min_periods=1) #{‘pearson’, ‘kendall’, ‘spearman’}
    R = corrcoef(spearman)
    pcolor(R)
    colorbar()
    #yticks(arange(0.5,10.5),range(0,10))
    #xticks(arange(0.5,10.5),range(0,10))
    show()

def prep_hinton(df): #2014 07 22
    """
    Visualizes a matrix with hinton diagram.
    
    Arguments:
    df - pandas dataframe object.
    
    Returns:
    Hinton diagram
    """
    
 #   plt.figure(figsize=(10, 10))
    sakos = df['skspvd'].unique()
    kryptys = df['krppvd'].unique()
    df2 = pd.DataFrame(index=sakos, columns=kryptys)

    for x in sakos:
        if len(df[df['skspvd'] == x].krppvd.values) > 0:
            for y in df[df['skspvd'] == x].krppvd.values:
                df2[y][x] = True

    df2.fillna(False,inplace=True)   
    spearman = df2.corr(method='spearman', min_periods=1) #{‘pearson’, ‘kendall’, ‘spearman’}
    return spearman
