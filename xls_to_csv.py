
import pandas
import os, os.path

def run(indir, outdir):
    for fname in os.listdir(indir):
        if not fname.endswith('.xls'):
            continue
        data = pandas.read_excel(os.path.join(indir, fname))
        csv_fname = fname[:-4] + '.csv'
        outfname = os.path.join(outdir, csv_fname)
        data.to_csv(outfname)

if __name__ == '__main__':
    run('temp', 'raw_csv')

            
