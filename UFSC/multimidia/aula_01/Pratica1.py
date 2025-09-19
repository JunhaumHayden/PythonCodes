# Aula prática de áudio digital
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample
from IPython.display import Audio, display
import ipywidgets as widgets
import os

def process_audio_advanced(filename, target_rate=44100, bits=16):
    # Ler arquivo original:
    # - original_rate -> taxa de amostragem em Hz
    # - audio_data -> um array NumPy contendo as amostras do áudio.
    # - audio_data.shape (1 ou 2): número de canais: 1D para mono e 2D para estéreo
    original_rate, audio_data = wavfile.read(filename)

    # Se estéreo, pegar apenas um canal
    if len(audio_data.shape) > 1:
        audio_data = audio_data[:,0]
        # Seleciona todas as linhas (:) e apenas a primeira coluna (0), ou seja, o canal esquerdo.

    # Altera a taxa de amostragem do áudio (resampling),
    # len(audio_data) → número total de amostras no áudio original.
    # original_rate → taxa de amostragem do áudio original (em Hz).
    # target_rate → nova taxa de amostragem desejada (em Hz).
    # Ajusta o número de amostras do áudio para a nova taxa de amostragem.
    num_samples = int(len(audio_data) * target_rate / original_rate)

    # gera o novo áudio com a taxa de amostragem selecionada
    audio_resampled = resample(audio_data, num_samples)

    #determina o maior valor de amostra
    max_val = np.max(np.abs(audio_resampled))

    # Normaliza o áudio:
    # - Divide cada amostra pelo valor absoluto máximo (max_val) do áudio resampleado.
    # - Resultado: valores entre -1 e 1, independentemente da amplitude original.
    audio_normalized = audio_resampled / max_val

    max_val = np.max(np.abs(audio_resampled))
    if bits == 8:
        # Converte para byte entre [0,255], onde 127 é zero
        audio_processed = np.uint8(audio_normalized*127 + 128)
    elif bits == 16:
        # Converte para int16 entre [-32767, +32767]
        audio_processed = np.int16(audio_normalized * 32767)
    elif bits == 4:
        # audio_processed: valores inteiros de -7 até +7 (15 níveis)
        audio_processed = np.round(audio_normalized * 7)
        # Reescala para [0, 14]
        audio_processed = audio_processed + 7
        # Mapeia para [0, 255]
        audio_processed = np.uint8(audio_processed * (255 // 14))
    else:
        raise ValueError("Bits permitidos: 4, 8 ou 16")

    # Salvar arquivo
    base, ext = os.path.splitext(filename)
    output_filename = f"{base}_{target_rate}Hz_{bits}bit.wav"
    wavfile.write(output_filename, target_rate, audio_processed)
    print(f"Arquivo salvo como: {output_filename}")

    if bits == 8 or bits == 4:
        # Antes de calcular a FFT, converta para float centrado em zero
        audio_processed = audio_processed.astype(np.float32)        # converte para float
        audio_processed = audio_processed - 128                     # remove offset DC
    fft_vals = np.fft.rfft(audio_processed)
    fft_freq = np.fft.rfftfreq(len(audio_processed), 1/target_rate)
    magnitude = np.abs(fft_vals)


    # Plot waveform
    plt.figure(figsize=(12, 3))
    time_axis = np.linspace(0, len(audio_processed)/target_rate, num=len(audio_processed))
    plt.plot(time_axis, audio_processed)
    plt.title(f"Waveform - Rate: {target_rate} Hz, Bits: {bits}")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

    # Plot espectro de frequência
    plt.figure(figsize=(12, 3))
    plt.plot(fft_freq, magnitude)
    plt.title(f"Frequency Spectrum")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.show()

    # Reproduzir áudio
    display(Audio(audio_processed, rate=target_rate))
if __name__ == '__main__':
    # Arquivo de áudio
    filename = "audio.wav"

    # Widget interativo
    widgets.interact(
        process_audio_advanced,
        filename=widgets.fixed(filename),
        target_rate=widgets.IntSlider(min=4000, max=44100, step=1000, value=8000, description="Sampling Rate"),
        bits=widgets.Dropdown(options=[4, 8, 16], value=8, description="Bits per Sample")
    )
