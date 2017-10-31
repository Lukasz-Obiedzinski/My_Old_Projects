__author__ = 'Lukasz Obiedzinski'
# Sygnal z sinusoidalna dwuwstegowa modulacja amplitudy DSB
# dane: czestotliwosc nosna, czetotliwosc sygnalu modulujacego, amplituda sygnalu modulujacego
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from pylab import *
import scipy.signal as signal
####################################################################
# -------- zmienne z zadania
# czestotliwosc_nosna = float(input('Podaj czestotliwosc nosna [Hz]: '))
# czestotliwosc_mod = float(input('Podaj czestotliwosc sygnalu modulujaca [Hz]: '))
# amp_mod = float(input('Podaj wartosc amplitudy sygnalu modulujacego [V]: '))
czestotliwosc_nosna = 2500
czestotliwosc_mod = 800
amp_mod = 2
# ------------------------
# znieksztalcenie w medium transmisyjnym
#znieksztalcenie_w_kanale =
# ________________________________________________________________
# szerokosc pasma sygnalu mod
czas_symulacji=500e-3
f_s = float(44100)
zmienna = 0.5
#####################################################################
# sprawdzenie czy zmienne sa dobrych wartosci
if czestotliwosc_nosna < 0:
    print('ZLA CZESTOTLIWOSC NOSNA')
    czestotliwosc_nosna = float(input('Podaj czestotliwosc nosna [Hz] : '))
else:
    print (czestotliwosc_nosna)
if czestotliwosc_mod < 0:
    print('ZLA CZESTOTLIWOSC MODULUJACA')
    czestotliwosc_mod = float(input('Podaj czestotliwosc modulujaca [Hz]:'))
else:
    print (czestotliwosc_mod)
if amp_mod < 0:
    print('ZLA AMPLITUDA MODULACJI')
    amp_mod = float(input('Podaj wartosc amplitudy modulujacej [Hz]: '))
else:
    print (amp_mod)
#####################################################################
# zdefiniowanie zmienny sygnalu
def prostokatny_sygnal(czestotliwosc, faza, czas_w):
    return np.sign(sinus_sygnal(amp_mod, czestotliwosc, faza, czas_w))
def sinus_sygnal(amp_mod,czestotliwosc, faza, czas_w):
    return np.sin(2*np.pi*(czestotliwosc)*czas_w+faza)
noise= np.random.normal(0,1,22050)
#####################################################################
# sygnaly
czas_w = np.linspace(0,czas_symulacji,czas_symulacji*f_s)
sygnal_wysylany1 = sinus_sygnal(amp_mod, czestotliwosc_nosna, 0, czas_w)
# sygnal_mod = prostokatny_sygnal(czestotliwosc_mod, 0, czas_w)
sygnal_mod = sinus_sygnal(0,czestotliwosc_mod, 0, czas_w)
sygnal2 = sygnal_wysylany1 + noise
#######################################################################
# - modulacja AM
Sygnal_nosny = amp_mod*sinus_sygnal(0,czestotliwosc_nosna,0,czas_w)
Sygnal_modulujacy = sygnal_mod/np.max(sygnal_mod)*zmienna
Sygnal_zmodulowany = Sygnal_nosny*(Sygnal_modulujacy+1)
sygnal_kanal = Sygnal_zmodulowany+noise
#######################################################################
# wykresy
# 1. Sygnal modulujacy
plt.figure(1)
plt.subplot(2, 2, 1)
plt.grid()
plt.plot(czas_w, sygnal_mod, 'r')
plt.title('Sygnal modulujacy - uzyteczny - sinus')
plt.xlabel('Czestotliwosc [Hz]')
plt.ylabel('Amplituda [dB]')
# 2. Kanal AWGN
plt.subplot(2, 2, 2)
plt.grid()
plt.plot(czas_w, sygnal_wysylany1, 'g')
plt.title('Sygnal nosny - Sinus')
plt.xlabel('Czestotliwosc [Hz]')
plt.ylabel('Amplituda [dB]')
plt.xlabel('Czestotliwosc [Hz]')
# 3. Sygnal sinusoidalny z szumem
plt.subplot(3, 1, 3)
plt.grid()
plt.title('Sygnal zmodulowany AM')
plt.plot(czas_w,Sygnal_zmodulowany,'b')
plt.ylabel('Amplituda [dB]')
# 4 Sygnal zmodulowany + szum
plt.figure(3)
plt.grid()
plt.title('Kanal komunikacyjny')
kanal_plot, =plt.plot(czas_w, sygnal_kanal, label='Sygnal w kanale',
color='b')
noise_plot, = plt.plot(czas_w, noise, label="Noise", linestyle='-',color='r')
zmodulowany_plot, = plt.plot(czas_w, Sygnal_zmodulowany, label="Sygnal_zmodulowany", linewidth=4 ,color='g')
plt.legend(handles=[kanal_plot,zmodulowany_plot, noise_plot])
plt.title('Sygnal zmodulowany AM w kanale AWGN')
plt.xlabel('Czestotliwosc [Hz]')
plt.ylabel('Amplituda [dB]')
##############################################################
# --- Wariancja i stosunek sygnalu do szumu
print ('Dla czestotliwosci nosnej = ',+czestotliwosc_nosna, '\n')
print ('Dla czestotliwosci sygnalu modulujacego = ',+czestotliwosc_mod,
'\n')
print ('Dla amplitudy sygnalu modulujacego = ',+amp_mod, '\n')
#wariancja oraz stosunek sygnalu do szumu
noise_squared=np.square(noise)
# noise_mean = np.mean(noise_squared)
wariancja_szumu= np.var(noise)
var_sygnal_zmodulowany = np.var(Sygnal_zmodulowany)
SNR_Zmodulowany_lin = var_sygnal_zmodulowany/wariancja_szumu
SNR_Zmodulowany = 10*np.log10(SNR_Zmodulowany_lin)
print ('Wariancja szumu oraz stosunek sygnalu zmodulowanego do szumu przed filtracja', '\n')
print ('Wariancja szumu = ' + str(wariancja_szumu))
print ('Stosunek sygnalu zmodulowanego do szumu = ' +str(SNR_Zmodulowany),
'dB')
########################################################
# --------------------------------------
# Nowe wykresy filtrow
f_s = float(44100)
dlugosc_filtru = 2049
czest_1 = 2.0e3
czest_2 = 3.5e3
Dlugosc = 16*1024
low_pass = signal.firwin(dlugosc_filtru, czest_1 , nyq=f_s /2)
splot_lowpass = np.convolve(low_pass, noise)
splot_lowpass_fft = np.fft.fft(splot_lowpass, Dlugosc)
LOW_PASS = np.abs(splot_lowpass_fft[0:Dlugosc/2])
band_pass = signal.firwin(dlugosc_filtru, [czest_1, czest_2] , nyq=f_s /2, pass_zero = False)
splot_bandpass =np.convolve(band_pass, noise)
splot_bandpass_fft = np.fft.fft(splot_bandpass, Dlugosc)
BAND_PASS = np.abs(splot_bandpass_fft[0:Dlugosc/2])
splot_bandpass_signal = np.convolve(band_pass, sygnal_wysylany1)
splot_bandpass_signal_fft = np.fft.fft(splot_bandpass_signal, Dlugosc)
BAND_PASS_signal = np.abs(splot_bandpass_signal_fft[0:Dlugosc/2])
sygnal_wysylany1_fft= np.fft.fft(sygnal_wysylany1, Dlugosc)
sygnal_wysylany1_fft_abs = np.abs(sygnal_wysylany1_fft[0:Dlugosc/2])
splot_sygnal2 = np.convolve(band_pass, sygnal2)
splot_sygnal2_fft = np.fft.fft(splot_sygnal2, Dlugosc)
BAND_PASS_signal2 = np.abs(splot_sygnal2_fft[0:Dlugosc/2])
roznica_sygnalow = sygnal_wysylany1_fft_abs - BAND_PASS_signal2
freq_x = np.linspace(0,0.5,Dlugosc/2)*f_s
# ----- splot sygnalu zmodulowanego z szumem z filtrem pasmowoprzepustowym; sygnal kanal
splot_zmodulowany_szum = np.convolve(band_pass, sygnal_kanal)
splot_zmodulowany_szum_fft = np.fft.fft(splot_zmodulowany_szum, Dlugosc)
splot_zmodulowany_szum_filtr =np.abs(splot_zmodulowany_szum_fft[0:Dlugosc/2])
# plt.figure(8)
# plt.grid()
# plt.title('Porownanie sygnalow przed i po filtracji ')
# plot_sygnal2, =plt.plot(freq_x,20*np.log10(BAND_PASS_signal2), label="Sin+noise_fil_bp", linestyle='-', color='b')
# plot_sygnal_wysylany, =plt.plot(freq_x,20*np.log10(sygnal_wysylany1_fft_abs), label="Sinus", linestyle='--', color='r')
# plot_roznica, =plt.plot(freq_x,(20*np.log10(roznica_sygnalow)), label="roznica", color='g')
# #plot_sinus_goly, = plt.plot(freq_x, sygnal2, 'c')
# plt.legend(handles=[plot_sygnal2, plot_sygnal_wysylany,plot_roznica])
plt.figure(4)
plt.grid()
plt.title('Sygnal w kanale AWGN po filtracji Bandpass')
plt.plot(freq_x,20*np.log10(splot_zmodulowany_szum_filtr))
plt.xlabel('Czestotliwosc [Hz]')
plt.ylabel('Amplituda [dB]')
# --- Wariancja i stosunek sygnalu w kanale do sygnalu po filtracji
sygnal_kanal_fft = np.fft.fft(sygnal_kanal, Dlugosc)
sygnal_kanal_fft_filtr = np.abs(sygnal_kanal_fft[0:Dlugosc/2])
var_sygnal_zmodulowany_fft_filtr=np.var(sygnal_kanal_fft_filtr)
wariancja_sygnal_kanal = np.var(splot_zmodulowany_szum_filtr)
SNR_kanal_filtr = var_sygnal_zmodulowany_fft_filtr/wariancja_sygnal_kanal
SNR_kanal_filtr_dB = 10*np.log10(SNR_kanal_filtr)
print ('Stosunek sygnalu przed filtracja do sygnalu po filtracji = '+str(SNR_kanal_filtr_dB), 'dB')
#http://mpastell.com/2010/01/18/fir-with-scipy/
#########################################################
# ----- Spektrum sygnalu przed kanalem i w kanale
plt.figure(5)
plt.grid()
plt.title("Spectrum sygnalow przed i po filtracji")
plot_sygnal_kanal_fft,=plt.plot(freq_x,20*np.log10(sygnal_kanal_fft_filtr), label="Sygnal zmodulowany w kanale", linewidth=2 ,color='r' )
plot_sygnal_kanal_filtr,=plt.plot(freq_x,20*np.log10(splot_zmodulowany_szum_filtr), label="Sygnal przefiltrowany", linewidth=2 ,color='g')
plot_sygnal_roznicowy, = plt.plot(freq_x,(20*np.log10(splot_zmodulowany_szum_filtr)- 20*np.log10(sygnal_kanal_fft_filtr)),
                                  label="Sygnal roznicowy", linewidth=1,color='b' )
plt.legend(handles=[ plot_sygnal_kanal_fft,
plot_sygnal_kanal_filtr,plot_sygnal_roznicowy])
plt.xlabel('Czestotliwosc [Hz]')
plt.ylabel('Amplituda [dB]')
#########################################################
# ------ Demodulacja
f_s = float(44100)
dlugosc_filtru = 2049
czest_1 = 2.0e3
czest_2 = 3.5e3
Dlugosc = 16*1024
# sqrt = np.square(sygnal_kanal [0:czas_symulacji*f_s])
czest_3 = 100
czest_4 = 500
# plt.plot(freq_x,20*np.log10(splot_zmodulowany_szum_filtr), 'r')
# plt.plot(czas_w,sqrt, 'g')
sqrt = np.square(sygnal_kanal)
low_pass = signal.firwin(dlugosc_filtru, czest_3 , nyq=f_s /2)
high_pass = signal.firwin(dlugosc_filtru, czest_4 , nyq=f_s /2,
pass_zero = False)
filtracja_LP = np.convolve(low_pass, np.square(sygnal_kanal))
filtracja_LP_fft = np.fft.fft(filtracja_LP, Dlugosc)
filtracja_LP_abs = np.abs(filtracja_LP_fft)[0:Dlugosc/2]
plt.figure(6)
plt.grid()
plt.plot(filtracja_LP, 'b')
plt.title('Demodulacja sygnalu')
plt.xlabel('Czestotliwosc [Hz]')
plt.ylabel('Amplituda [dB]')
# filtracja_HP = np.convolve(high_pass, filtracja_LP)
# filtracja_HP_fft = np.fft.fft(filtracja_HP, Dlugosc)
# filtracja_HP_abs = np.abs(filtracja_HP_fft)[0:Dlugosc/2]
#
# plt.figure(7)
# plt.plot(filtracja_HP)
# analiza widmowa
# from numpy.fft import fft, fftshift
#
# spectrum = fft(sygnal_wysylany1 ,len(sygnal_wysylany1))
# spectrum = abs(spectrum)
#
# freq_vec2 = np.linspace(0,f_s,f_s/10)
#
# plt.figure(2)
# plt.grid()
# plt.plot(freq_vec2, 20*np.log10(abs(spectrum)[0:f_s/10]))
# plt.title('Analiza widmowa')
# plt.xlabel('Czestotliwosc [Hz]')
# plt.ylabel('Amplituda [dB]')
# # #
# -------------------------------------------------------------------------

# - Sygnal do szumu WEJ/WYJ Wszystkie błedy
var_sygnal_po_filtracji = np.var(splot_zmodulowany_szum_filtr)
var_sygnal_po_demodulacji = np.var(filtracja_LP)
SNR_IN_OUT_lin= var_sygnal_po_filtracji/var_sygnal_po_demodulacji
SNR_IN_OUT = 10*np.log10(SNR_IN_OUT_lin)
print ('Moc sygnału na wejsciu = '+str(np.square(sygnal_kanal)), 'dB')
print ('SNR IN/OUT = '+str(SNR_IN_OUT), 'dB')
print ('Stosunek dlugosci syg IN/Out ='+(str(len(filtracja_LP)/len(sygnal_kanal))))
#############################################################
# audio
rate, data = wavfile.read("cos.wav")
print ('Czestotliwosc probki',rate)
print ('Dlugosc probki',len(data))
plt.show()