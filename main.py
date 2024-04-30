import os
import pandas as pd
import shutil
import qrcode

# Get the current working directory
cwd = os.getcwd()

# Read CSV file
df = pd.read_csv(os.path.join(cwd, 'assets/Data/Interviewers Name and ID Photo.csv'))

# Path to the folder containing images
image_folder_path = os.path.join(cwd, 'assets/Data/Images')

source_css_path = '/Users/thilakna/Documents/GitHub/ChanukaRavishan.github.io/assets/css'

source_about_path = '/Users/thilakna/Documents/GitHub/ChanukaRavishan.github.io/assets/images'

qr_path = '/Users/thilakna/Documents/GitHub/ChanukaRavishan.github.io/QRs'
# List to store nic and corresponding URLs
nic_urls = []

for file in os.listdir(image_folder_path):
    if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        nic = file.split('.')[0]
        name_row = df[df['NIC'] == nic]
        if not name_row.empty:
            name = name_row.iloc[0]['Name']
            # Create folder if not exists
            folder_name = name.replace(' ', '_')
            folder_path = os.path.join(folder_name)
            os.makedirs(folder_path, exist_ok=True)
            # Move image file to the folder
            assets_path = os.path.join(folder_path, 'assets/Data/Images')
            os.makedirs(assets_path, exist_ok=True)
            shutil.move(os.path.join(image_folder_path, file), os.path.join(assets_path, file))
            destination_assets_path = os.path.join(folder_path, 'assets')
            shutil.copytree(source_css_path, os.path.join(destination_assets_path, 'css'))
            # Copy images folder to assets folder
            shutil.copytree(source_about_path, os.path.join(destination_assets_path, 'images'))
            # Create and save HTML file

            # Generate HTML content
            html_content = f"""
            <!doctype html>
            <html class="no-js" lang="en">
            <head>
                <!-- meta data -->
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <!-- title of site -->
                <title>LECO survey</title>
                <!-- style sheets -->
                <link rel="stylesheet" href="assets/css/font-awesome.min.css">
                <link rel="stylesheet" href="assets/css/animate.css">
                <link rel="stylesheet" href="assets/css/bootstrap.min.css">	
                <link rel="stylesheet" href="assets/css/style.css">
                <link rel="stylesheet" href="assets/css/responsive.css">
            </head>
            <body>
                <section id="welcome-hero" class="">
                    <div class="container">
                        <img src="assets/images/about/welcome-banner.png" alt="Welcome Image">
                    </div>
                </section>
                <section id="welcome-hero-2" class="welcome-hero-2">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-12 text-center">
                                <div class="header-text">
                                    <h2>LECO ගෘහස්ත විදුලි පරිභෝජන සමීක්ෂණයට සාදරයෙන් පිළිගනිමු!
                                        <br>Welcome to the LECO Household Electricity Consumption Survey!
                                        <br>LECO வீட்டு மின் நுகர்வு ஆய்வுக்கு வரவேற்கிறோம்!
                                    </h2>
                                    <div class="container">
                                        <br> 
                                        <h3>Enumerator</h3>
                                        <img src="assets/Data/Images/{file}" alt="Enumerator ID" style="width: 200px; height: 200px;">
                                        <br>
                                        <h3>
                                            Name: {name}
                                            <br>
                                            NIC: {nic}
                                        </h3>
                                        <h3>
                                            ඔබ නිවසේ විදුලිය භාවිතා කරන ආකාරය අවබෝධ කර ගැනීමට අපි LIRNEasia සමඟ මෙම සමීක්ෂණය දියත් කර ඇත. ඔබගේ පුරුදු සහ විදුලිය භාවිතා කිරීමේ රටා අවබෝධ කර ගැනීම අපගේ සේවාවන් වැඩිදියුණු කිරීමට සහ විශ්වාසනීය බල සැපයුමක් සහතික කිරීමට උපකාරී වේ. නිල හැඳුනුම්පත් සහ ලිපි වලින් සමන්විතව ඔබගේ නිවසට පැමිණ ඇති Survey Research Lanka (SRL) හි ඉහත සදහන් මහත්මා හෝ මහත්මිය, ඔබේ නිවස සහ ඔබ විදුලිය භාවිතා කරන ආකාරය ගැන විමසනු ඇත. අපට ඔබට වඩා හොඳ සේවාවක් සැපයිය හැකි ආකාරය වඩා හොඳින් අවබෝධ කර ගැනීමට දරන මේ වෑයම සාර්ථක කර ගැනීමට ඔවුන් සමග සහයෝගයෙන් කටයුතු කරන මෙන් කාරුණිකව ඉල්ලා සිටිමු.
                                            <br>
                                            <br>We're working with LIRNEasia to understand how you use electricity at home in Sri Lanka. Understanding your habits and patterns of using electricity helps us improve our services and ensure a reliable power supply. The above representative from Survey Research Lanka (SRL), equipped with a official ID card and a letter from us, will ask about your household and how you use electricity. Please cooperate with them to help us better understand how we can provide you with better service.
                                            <br>
                                            <br>இலங்கையில் நீங்கள் வீட்டில் மின்சாரத்தை எவ்வாறு பயன்படுத்துகிறீர்கள் என்பதைப் புரிந்துகொள்ள LIRNEasia உடன் இணைந்து பணியாற்றி வருகிறோம். உங்கள் பழக்கவழக்கங்கள் மற்றும் மின்சாரத்தைப் பயன்படுத்தும் முறைகளைப் புரிந்துகொள்ளும் மூலம், எங்கள் சேவைகளை மேம்படுத்தவும் நம்பகமான மின்சார விநியோகத்தை உறுதிப்படுத்தவும் உதவுகிறது. உத்தியோகபூர்வ அடையாள அட்டைகள் மற்றும் எங்களிடமிருந்து கடிதங்களுடன் கூடிய சர்வே ரிசர்ச் லங்காவின் (SRL) மேற்கண்ட பிரதிநிதி, உங்கள் வீடு மற்றும் நீங்கள் மின்சாரத்தை எவ்வாறு பயன்படுத்துகிறீர்கள் என்பதைப் பற்றி கேட்பார். உங்களுக்கு சிறந்த சேவையை நாங்கள் எவ்வாறு வழங்குவது என்பதை நாங்கள் நன்கு புரிந்துகொள்ள அவர்களுடன் ஒத்துழைக்கவும்.
                                        </h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                <script src="assets/js/jquery.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
                <script src="assets/js/bootstrap.min.js"></script>
                <script src="assets/js/bootsnav.js"></script>
                <script src="assets/js/jquery.sticky.js"></script>
                <script src="assets/js/owl.carousel.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js"></script>
                <script src="assets/js/custom.js"></script>
            </body>
            </html>"""

            with open(os.path.join(folder_path, "index.html"), "w") as html_file:
                html_file.write(html_content)
            print('done')
            print(nic)
            html_url = f"https://lecoapp.leco.lk/{folder_name}/index.html"
            # Append to the list
            nic_urls.append({'NIC': nic, 'URL': html_url})
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(html_url)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")
            qr_img.save(os.path.join(qr_path, f"{nic}_{name}_qr.png"))

            



        else:
            print(f"No corresponding name found for NIC: {nic}")


        # Convert the list of dictionaries to a DataFrame
nic_urls_df = pd.DataFrame(nic_urls)

# Save the DataFrame to a CSV file
nic_urls_df.to_csv('nic_urls.csv', index=False)
