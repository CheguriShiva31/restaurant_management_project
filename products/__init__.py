<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Restaurant Homepage</title>
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
   <link rel="stylesheet" href="{%static 'css/styles.css'%}">
   </head>
   <body class="bg-light text-dark">

   <nav class="navbar navbar-expand-lg navbar-dark bg-danger">
   <div class="container">
   <a class="navbar-brand fw-bold" href="#"> My Restaurant</a> </div>
   <a href="/" class="nav-link text-white"> Home</a>
   <a href="/ about" class="nav-link text-white"> About</a> </div>
    
    </nav>
    <header class="text-center py-5 bg-warning text-dark">
    <h1 class="display-4 fw-bold"> Welcome to my Restaurant</h1>
    <p class="lead"> Delicious food, friendly service, and cozy vibes</p>
    <a href="menu" class="btn btn-danger btn-lg"> View Menu</a>
     </header>
     <main class="container my-5">
     <div class="row">
     <div class="col-md-6">
     <h2>our specialities</h2>
     <p> We serve freshly prepared dishes with locally sourced ingredients.</p>
         <div class="col-md-6">
         <img src="{% static 'image/restaurant.jpg' %}" class="img-fluid rounded shadow" alt="Restaurant">
         </div>
         <footer class="text-center py-3 bg-dark text-white">
         &copy; 2025 My Restaurant. All rights resvered.
           </footer>
           </body>
           </html>



#css

body {font-family:'segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
h1,h2 {letter-spacing: 1px;}
header{background: liner-gradient(45deg,#ffc107, #ff9800);}
footer{font-size:0.9rem;}
