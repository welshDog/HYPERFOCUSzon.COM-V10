#!/bin/bash

# 🚀💎 HYPERFOCUS ZONE PORTALS - MINI SERVER DEPLOYMENT 💎🚀
# Deploy showcase portals to mini server (217.154.42.40 / 100.71.69.16)

echo "🌟⚡💎 DEPLOYING SHOWCASE PORTALS TO MINI SERVER 💎⚡🌟"
echo "Target: Mini Server (100.71.69.16)"
echo "=================================================="

# 1. Create web directory structure on mini server
echo "📁 Setting up web directories..."
ssh root@217.154.42.40 "mkdir -p /var/www/showcase/{admin,creator,portfolio}"

# 2. Upload portal files
echo "📤 Uploading showcase portals..."
scp portals/admin-portal-showcase.html root@217.154.42.40:/var/www/showcase/admin/index.html
scp portals/creator-portal-showcase.html root@217.154.42.40:/var/www/showcase/creator/index.html  
scp portals/showcase-portal-demo.html root@217.154.42.40:/var/www/showcase/portfolio/index.html

# 3. Upload README as main landing page
echo "📖 Creating main landing page..."
ssh root@217.154.42.40 "cat > /var/www/showcase/index.html" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀💎 LEGENDARY EMPIRE SHOWCASE 💎🚀</title>
    <style>
        body { 
            font-family: 'Segoe UI', sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; color: #fff; margin: 0; padding: 40px;
        }
        .container { max-width: 800px; margin: 0 auto; text-align: center; }
        .header { background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; 
                 backdrop-filter: blur(15px); margin-bottom: 40px; }
        .portals { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
        .portal-card { background: rgba(255,255,255,0.15); padding: 30px; border-radius: 15px;
                      backdrop-filter: blur(10px); transition: transform 0.3s; }
        .portal-card:hover { transform: translateY(-5px); }
        .portal-link { color: #fff; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀💎 LEGENDARY EMPIRE SHOWCASE 💎🚀</h1>
            <p>ADHD-Friendly AI-Powered Development Empire</p>
            <p><strong>Mini Server Node:</strong> 100.71.69.16</p>
        </div>
        <div class="portals">
            <div class="portal-card">
                <h3>🏛️ Admin Portal</h3>
                <p>Empire Operations</p>
                <a href="/admin/" class="portal-link">Enter Portal →</a>
            </div>
            <div class="portal-card">
                <h3>🧠 Creator Portal</h3>
                <p>AI Content Hub</p>
                <a href="/creator/" class="portal-link">Enter Portal →</a>
            </div>
            <div class="portal-card">
                <h3>🌟 Portfolio</h3>
                <p>Project Showcase</p>
                <a href="/portfolio/" class="portal-link">Enter Portal →</a>
            </div>
        </div>
    </div>
</body>
</html>
EOF

# 4. Configure Nginx to serve the showcase
echo "⚙️ Configuring Nginx..."
ssh root@217.154.42.40 "cat > /etc/nginx/sites-available/showcase" << 'EOF'
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    
    root /var/www/showcase;
    index index.html;
    
    server_name _;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    location /admin/ {
        alias /var/www/showcase/admin/;
        try_files $uri $uri/ /admin/index.html;
    }
    
    location /creator/ {
        alias /var/www/showcase/creator/;
        try_files $uri $uri/ /creator/index.html;
    }
    
    location /portfolio/ {
        alias /var/www/showcase/portfolio/;
        try_files $uri $uri/ /portfolio/index.html;
    }
}
EOF

# 5. Enable the site and restart Nginx
echo "🔄 Activating showcase site..."
ssh root@217.154.42.40 "ln -sf /etc/nginx/sites-available/showcase /etc/nginx/sites-enabled/default"
ssh root@217.154.42.40 "nginx -t && systemctl reload nginx"

# 6. Set proper permissions
echo "🔐 Setting permissions..."
ssh root@217.154.42.40 "chown -R www-data:www-data /var/www/showcase"
ssh root@217.154.42.40 "chmod -R 755 /var/www/showcase"

echo "✅ DEPLOYMENT COMPLETE!"
echo "🌐 Access your showcase at:"
echo "   • Main Portal: http://100.71.69.16"
echo "   • Admin Portal: http://100.71.69.16/admin/"
echo "   • Creator Portal: http://100.71.69.16/creator/"
echo "   • Portfolio: http://100.71.69.16/portfolio/"
echo "🎉 EMPIRE SHOWCASE IS LIVE ON MINI SERVER! 🎉"
