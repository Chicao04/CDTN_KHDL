from audio_compare import AudioComparator
import os

def test_audio_comparison():
    # Khởi tạo đường dẫn
    project_root = "D:\\filebailam\\CD3_Giongnoi\\code_speech"
    
    # Chọn 1 file để test
    emotion = "angry"
    filename = "03-01-05-01-01-01-05.wav" # Thay đổi tên file phù hợp
    
    original_path = os.path.join(project_root, "data", "RAVDESS", emotion, filename)
    processed_path = os.path.join(project_root, "data", "RAVDESS_processed", emotion, f"processed_{filename}")
    
    # Kiểm tra file tồn tại
    if not os.path.exists(original_path):
        print(f"File gốc không tồn tại: {original_path}")
        return
    if not os.path.exists(processed_path):
        print(f"File đã xử lý không tồn tại: {processed_path}")
        return
        
    # So sánh
    comparator = AudioComparator()
    
    # Load files
    original, processed = comparator.load_pair(original_path, processed_path)
    
    # Hiển thị so sánh
    print("\n=== So sánh file audio ===")
    print(f"File gốc: {filename}")
    print(f"File đã xử lý: processed_{filename}")
    
    comparator.compare_waveforms(original, processed)
    comparator.compare_specs(original, processed)
    comparator.print_stats(original, processed)
    comparator.play_audio(original, processed)

if __name__ == "__main__":
    test_audio_comparison()