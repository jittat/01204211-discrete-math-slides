import os
import os.path

def build(fname, template, outpattern):
    if fname.endswith('tex'):
        fname = '.'.join(fname.split('.')[:-1])
    texout_fname = outpattern % fname
    f = open(texout_fname,"w")

    template_filename = os.path.join(os.path.dirname(__file__),template)
    for l in open(template_filename).readlines():
        nl = l.replace("##",fname)
        f.write(nl)
    f.close()
    os.system('pdflatex %s' % texout_fname)
    os.remove(texout_fname)
