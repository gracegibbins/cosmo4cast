
import healpy as hp
import numpy as np
import matplotlib.pyplot as plt

 
nside = 1024


 
# nbar_str = nbar / hp.nside2pixarea(nside, degrees=False)
# print ("nbar = %g galaxies/arcmin^2"%(nbar_str*(np.pi/(180*60))**2)) 
 
#defining noise properties:
sigmae= 0.26
ndensity= 1.78 #1/arcmin2)
nshear_str = ndensity/((np.pi/(180*60))**2)
nl_gamma_noise =  np.ones(3*nside+1)* ((0.26**2)/(nshear_str))

npix_lens =  [2.25, 3.11,3.09, 2.61, 2.0]
nbar_lens = [npix_lens[i]/((np.pi/(180*60))**2) for i in range(5)]
shotnoise_lens = [(1. / nbar_lens[i])*np.ones(3*nside+1)  for i in range(5)]

#CMb lensing noise power spectrum
nlkk_cmb = np.load('/data/des91.b/data/gmarques/th_input/N0_CMBS4_MV.npy')
  
#paths
 
path_out = '/data/des91.b/data/gmarques/mocks/' #where the mocks are located
path_cls = '/home/s1/ggibbins/varyparams/noise_ps/' # Edit here where you want to save it!

def make_sim(seed): #seed # = # of relizations of maps from a ps/single cosmology for all
    np.random.seed()
    kcmb_sim = hp.read_map(path_out+'kcmb_sim_'+str(seed)+'.fits') #CMB ps without noise
    noise_kk_cmb = hp.synfast(nlkk_cmb,nside) #CMB noise creates map from cl
    clkcmb  = hp.anafast(kcmb_sim+noise_kk_cmb) #CMB ps WITH noise
    np.save(path_cls+'cl_kcmb_'+str(seed)+'.npy', clkcmb) #3072 x 1 array of ps values - l modes like 3 x nside or somethin
    
    clgg_all = []
    clkg_all = [] 
    for i in range(5): #loop for each number of z-bin
        lens_gal = hp.read_map(path_out+'gal_sim_z'+str(i)+'_sim_'+str(seed)+'.fits') #gal map
        nl_lens_gal = hp.synfast(shotnoise_lens[i],nside) #creates map of shotnoise
        cltotal_lens= hp.anafast(lens_gal+nl_lens_gal) #ps from gal & shotnoise map
        clgg_all.append(cltotal_lens) 
        clkg = hp.anafast(lens_gal+nl_lens_gal, map2=(kcmb_sim+noise_kk_cmb)) #ps of cross gal & cmb with noise
        clkg_all.append(clkg)
    np.save(path_cls+'clgg_allz_'+str(seed)+'.npy', np.array(clgg_all))
    np.save(path_cls+'clkcmbg_allz_'+str(seed)+'.npy', np.array(clkg_all))
    clgamma_all = []
    clkgamma_all = [] 
    for j in range(5):
        source_gal = hp.read_map(path_out+'source_gal_sim_z'+str(j)+'_sim_'+str(seed)+'.fits')
        nl_kappagal = hp.synfast(nl_gamma_noise, nside)
        cltotal_source= hp.anafast(source_gal+nl_kappagal) #wl ps with gamma noise
        clgamma_all.append(cltotal_source)
        clkkgal = hp.anafast(source_gal+nl_kappagal, map2=(kcmb_sim+noise_kk_cmb)) #ps of cross wl & cmb with noise
        clkgamma_all.append(clkkgal)
    np.save(path_cls+'clkkgal_allz_'+str(seed)+'.npy', np.array(clgamma_all))
    np.save(path_cls+'clkcmbkgal_allz_'+str(seed)+'.npy', np.array(clkgamma_all))




from multiprocessing import Pool 
import os, multiprocessing, time
if __name__ == '__main__':
    from multiprocessing.pool import ThreadPool as Pool
    pool = Pool(10)
    print(pool.map(make_sim, range(2000))) #runs this 2000 times in parallel -- 10,000 ps
 

