# weather-notifier

This is a weather notification script for Windows 10. You can get weather notifications with small configurations on your computer. I used [OpenWeather](https://openweathermap.org/) API to fetch data. That's why if you want to run this project, you need to have a API Key. You can [register](https://home.openweathermap.org/users/sign_up) and get API Key from [here](https://openweathermap.org/price). 

# Requirements

- `python3.x`
- `requests`
- `win10toast`

You can install libraries as follow:

`$ pip install requests`

`$ pip install win10toast`

# How to run?

Firstly, you need to clone this repository. To clone the repository, you can run following command. 

```powershell
$ git clone git@github.com:gozeloglu/weather-notifier.git
```

Before running the script, be sure that you already installed above libraries. You can check the libraries by using following commands. 

```powershell
$ python3
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from win10toast import ToastNotifier
>>> 
```

If you don't get any error, it means that you have installed the libraries successfully.

Before configuration, you need to save the [OpenWeather API Key](https://openweathermap.org/api) and the city name that you want to get the notification to your environment. You can save environment variables in Windows 10 as follow:

1. Open the Start Search, type in **env**, and choose **Edit the system environment variables**.
2. Click the **Environment Variables…** button.
3. Click the **Environment Variables…** button.
4. Set the environment variables as needed.
    - You need to save API Key with **WEATHER_API_KEY**.
    - You need to save the city name with **CITY**. 

You can be sure that env variables are saved or not with the following command. To run the commands, open a new command prompt.

```powershell
> echo %WEATHER_API_KEY%
> echo %CITY%
```

You should see the key and city name that you saved on the system. 

If you did not face any problem, you can run the script with the following command. 
```powershell
$ python weather.py
```

If you will get the notification successfully, you can continue with the following steps. 

Finally, you need to schedule a task by using **Task Scheduler** in Windows 10. 

1. Open the Start Search, type in **Task Scheduler** and choose it. 
2. Select **Actions** on top of the window.
3. Select **Create Task** on the menu.
4. Give a name to your task on the **General**.
5. Select **Trigers** and **New**, respectively.
6. Determine your repeat time. Click **OK**.
7. Then, select **Actions** and **New**, respectively.
8. Select **Browse** and determine the `weather.pyw` full path. Click **OK** and close the windows. Everything that's all!

## Why we use `weather.pyw` instead of `weather.py`?

If you select `weather.py` as the script file, the Python console will pop-up when the script is run. In order to block this pop-up console, we are using `weather.pyw` file. 

# Example

![Example](https://github.com/gozeloglu/weather-notifier/example/example.jpg)

# Contributions

Contributions are welcomed. If you face any issue or want to add a new feature, you can open an issue. 

# LICENSE