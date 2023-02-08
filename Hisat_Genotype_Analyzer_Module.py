import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def read_and_filter(file, threshold=10):
    
    gene_list, alel_list, abun_list = [], [], []
    with open(file) as infile:
        for line in infile:
            if 'abundance' in line:
                gene = line.strip().split(' ')[2].split('*')[0]
                alel = line.strip().split(' ')[2].split('*')[1]
                abun = float(line.strip().split(' ')[4].split('%')[0])
                
                if abun >= threshold:
                    gene_list.append(gene)
                    alel_list.append(alel)
                    abun_list.append(abun)
                    
    gene_alel_abun_dict = {'Gene':gene_list, 'Variant':alel_list, 'Abundance':abun_list}
    
    filtered_df = pd.DataFrame.from_dict(gene_alel_abun_dict)
    
    return filtered_df
    
def write_2_excel(df, filename, genes='All'):
    if genes == 'All':
        df.to_excel(filename[:-4]+'.xlsx', index=False)
    else:
        df_subset = df[df['Gene'].isin(genes)]
        df_subset.to_excel(filename[:-4]+'_subset.xlsx', index=False)
        
def plot_variants(df, gene='All'):
    
    df['Gene_Var'] = df.Gene + ':' + df.Variant
    
    if gene == 'All':
        sns.set(rc={'figure.figsize':(11.7,11.27)})
        sns.barplot(data = df, x = 'Abundance', y = 'Gene_Var')
        
    else:
        df_subset = df[df['Gene'] == gene]
        plt.pie(df_subset.Abundance, labels=df_subset.Variant, autopct='%.0f%%')
        plt.title(f"Variant abundances for gene {gene}")
        
def hisat_genotype_analyzer(file, mode, threshold=10, genes='All'):
    """
    Этот модуль анализирует результаты выполнения программы hisat-genotype
    param: file: input file
    param: mode: режим работы (write/plot)
    """
    
    hisat_genotype_df = read_and_filter(file, threshold)
    
    if mode == 'write' or mode == 'excel':
        write_2_excel(hisat_genotype_df, file, genes)
        
    elif mode == 'plot' or mode == 'figure' or mode == 'fig':
        plot_variants(hisat_genotype_df, genes)
        
    else:
        print(f'I can not do {mode}')
        print('Chose one of the existing modes: wrte or plot')
        