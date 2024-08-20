import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # ลบแถวที่ไม่มีค่าในคอลัมน์ 'url'
    df = df.dropna(subset=['url'])

    # แยกข้อมูล latitude และ longitude จาก 'url'
    df.loc[:, 'latitude'] = df['url'].apply(lambda x: x.split('!3d')[1].split('!')[0] if '!3d' in x else None)
    df.loc[:, 'longitude'] = df['url'].apply(lambda x: x.split('!4d')[1].split('!')[0] if '!4d' in x else None)

    # เลือกเฉพาะคอลัมน์ที่ต้องการ
    df_filtered = df[['name', 'description', 'location', 'latitude', 'longitude', 'category', 'service_option1', 'service_option2']]

    return df_filtered

def save_data(df, file_path, file_type='csv'):
    if file_type == 'csv':
        df.to_csv(file_path, index=False)
    elif file_type == 'json':
        df.to_json(file_path, orient='records')
    else:
        raise ValueError("Unsupported file type. Use 'csv' or 'json'.")

def main(input_file, output_file, output_type='csv'):
    # อ่านข้อมูล
    df = read_data(input_file)

    # ทำความสะอาดข้อมูล
    df_cleaned = clean_data(df)

    # บันทึกข้อมูลที่ทำความสะอาดแล้ว
    save_data(df_cleaned, output_file, output_type)

if __name__ == "__main__":
    # ตั้งค่าพาธไฟล์นำเข้าและไฟล์ออก พร้อมระบุชนิดไฟล์
    input_file = 'google_renamed.csv'  # เปลี่ยนเป็นพาธไฟล์ของคุณ
    output_file = 'google_cleaned.csv'  # เปลี่ยนเป็นพาธไฟล์ของคุณ
    output_type = 'csv'  # หรือ 'json' หากต้องการบันทึกเป็น JSON

    main(input_file, output_file, output_type)
