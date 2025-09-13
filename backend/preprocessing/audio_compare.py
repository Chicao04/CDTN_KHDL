import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from IPython.display import Audio
import soundfile as sf

class AudioComparator:
    def __init__(self):
        plt.rcParams['figure.figsize'] = [12, 6]
        
    def load_pair(self, original_path: str, processed_path: str):
        """Load cặp file audio gốc và đã xử lý"""
        audio_org, sr_org = librosa.load(original_path, sr=None)
        audio_proc, sr_proc = librosa.load(processed_path, sr=None)
        
        return (audio_org, sr_org), (audio_proc, sr_proc)
    
    def compare_waveforms(self, original: tuple, processed: tuple):
        """So sánh dạng sóng"""
        audio_org, sr_org = original
        audio_proc, sr_proc = processed
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 8))
        
        # Plot original
        librosa.display.waveshow(audio_org, sr=sr_org, ax=ax1)
        ax1.set_title("Dạng sóng file gốc")
        ax1.set_xlabel("Thời gian (s)")
        ax1.set_ylabel("Biên độ")
        
        # Plot processed
        librosa.display.waveshow(audio_proc, sr=sr_proc, ax=ax2)
        ax2.set_title("Dạng sóng file đã xử lý")
        ax2.set_xlabel("Thời gian (s)")
        ax2.set_ylabel("Biên độ")
        
        plt.tight_layout()
        plt.show()
        
    def compare_specs(self, original: tuple, processed: tuple):
        """So sánh phổ tần số"""
        audio_org, sr_org = original
        audio_proc, sr_proc = processed
        
        plt.figure(figsize=(15, 8))
        
        # Plot original spectrogram
        plt.subplot(2, 1, 1)
        D_org = librosa.amplitude_to_db(np.abs(librosa.stft(audio_org)), ref=np.max)
        librosa.display.specshow(D_org, sr=sr_org, x_axis='time', y_axis='hz')
        plt.colorbar(format='%+2.0f dB')
        plt.title("Phổ tần số file gốc")
        
        # Plot processed spectrogram  
        plt.subplot(2, 1, 2)
        D_proc = librosa.amplitude_to_db(np.abs(librosa.stft(audio_proc)), ref=np.max)
        librosa.display.specshow(D_proc, sr=sr_proc, x_axis='time', y_axis='hz')
        plt.colorbar(format='%+2.0f dB')
        plt.title("Phổ tần số file đã xử lý")
        
        plt.tight_layout()
        plt.show()
        
    def print_stats(self, original: tuple, processed: tuple):
        """In thống kê so sánh"""
        audio_org, sr_org = original
        audio_proc, sr_proc = processed
        
        print("\n=== Thống kê so sánh ===")
        print(f"File gốc:")
        print(f"- Sample rate: {sr_org} Hz")
        print(f"- Độ dài: {len(audio_org)/sr_org:.2f} giây")
        print(f"- Biên độ min/max: {audio_org.min():.3f}/{audio_org.max():.3f}")
        print(f"- RMS energy: {np.sqrt(np.mean(audio_org**2)):.3f}")
        
        print(f"\nFile đã xử lý:")
        print(f"- Sample rate: {sr_proc} Hz")
        print(f"- Độ dài: {len(audio_proc)/sr_proc:.2f} giây")
        print(f"- Biên độ min/max: {audio_proc.min():.3f}/{audio_proc.max():.3f}")
        print(f"- RMS energy: {np.sqrt(np.mean(audio_proc**2)):.3f}")
        
    def play_audio(self, original: tuple, processed: tuple):
        """Phát audio để so sánh"""
        audio_org, sr_org = original
        audio_proc, sr_proc = processed
        
        print("\nFile gốc:")
        # display(Audio(audio_org, rate=sr_org))
        
        print("\nFile đã xử lý:")
        # display(Audio(audio_proc, rate=sr_proc))

def main():
    # Khởi tạo đường dẫn
    project_root = "D:\\filebailam\\CD3_Giongnoi\\code_speech"
    
    # Chọn 1 file để test
    emotion = "angry"
    filename = "0001_000352.wav"
    
    original_path = os.path.join(project_root, "data", "Emotion", emotion, filename)
    processed_path = os.path.join(project_root, "data", "processed", emotion, f"processed_{filename}")
    
    # Kiểm tra file tồn tại
    if not os.path.exists(original_path) or not os.path.exists(processed_path):
        print("File không tồn tại!")
        return
        
    # So sánh
    comparator = AudioComparator()
    
    # Load files
    original = comparator.load_pair(original_path, processed_path)
    processed = comparator.load_pair(original_path, processed_path)
    
    # So sánh các khía cạnh
    comparator.compare_waveforms(original, processed)
    comparator.compare_specs(original, processed)
    comparator.print_stats(original, processed)
    comparator.play_audio(original, processed)

if __name__ == "__main__":
    main()