{% load static %}
<!doctype html>
<html lang="en">
<head>
 <meta charset="utf-8" />
 <meta name="viewport" content="width=device-width,initial-scale=1" />
 <title>page not found - 404<title>
 <link rel="stylesheet" href="{%static 'css/404.css'%">
 </head>
 <body>
   <main class="notfound">
   <div class="card">
   <div class="art">
   <svg width="160" heigth="120" viewBox="0 0 160 120"  aria-hidden="true">
   <rect x="8" y="8" rx="12" fill="#f6f8fb"/>
   <g transform="translate(36,20)">
   <circle cx="28" cy="28" r="28" fill="#f4f7ff"/>
           <text x="28" y="35" text-anchor="middle" font-family="sans-serif" fint-size="22 fill="#9aa7ff">404</text>
   </g>
   <rect x="72" y="24" width="60" height="10" rx="5" fill="#e7ecff"/>
       </svg>
    </div>

     <h1>page not found</h1>
     <p class="lead">We can't find tehpage you're looking for. It might have been moved or the link is broken.</p>
     
     <div class="actions">
     <a class="btn" href="{% url 'home'%}">Go to homepage</a>
     <a class="muted" href="javascript:history.back()">Go back</a>
        </div>
        <p class="hint">Tip: check the URL for typos or use the menu to navigate.</p>
        </div>
        </main>
        </body>
        </html>
    
]