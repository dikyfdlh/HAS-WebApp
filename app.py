from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'harsha_ananta_secret_key'

# Route untuk halaman beranda
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk halaman tentang kami
@app.route('/about')
def about():
    return render_template('about.html')

# Route untuk halaman layanan
@app.route('/services')
def services():
    return render_template('services.html')

# Route untuk halaman portfolio
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Route untuk halaman kontak
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route untuk menangani pengiriman form kontak
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        subject = request.form['subject']
        message = request.form['message']
        
        # Simpan pesan ke file atau database
        # Contoh sederhana: simpan ke file
        contact_dir = 'contacts'
        if not os.path.exists(contact_dir):
            os.makedirs(contact_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{contact_dir}/contact_{timestamp}_{name}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Nama: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Telepon: {phone}\n")
            f.write(f"Perusahaan: {company}\n")
            f.write(f"Subjek: {subject}\n")
            f.write(f"Pesan: {message}\n")
            f.write(f"Waktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Kirim flash message
        flash('Pesan Anda telah berhasil dikirim. Kami akan menghubungi Anda segera!', 'success')
        
        # Redirect kembali ke halaman kontak
        return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)