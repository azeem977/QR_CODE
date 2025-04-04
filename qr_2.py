import qrcode  

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,  
    border=4  
)

# Add data to the QR code
qr.add_data('https://chatgpt.com/c/67e432d3-d36c-8007-8a64-33ceb4a2e295')  
qr.make(fit=True)  

# Generate QR code image with custom colors
img = qr.make_image(fill_color='aqua', back_color='white')  

# Save the QR code image
img.save('chatgpt_qr.png')  

print('QR code saved as chatgpt_qr.png')

 
