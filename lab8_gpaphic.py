import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Đọc dữ liệu từ tệp data.txt và settings.txt
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")] 
data_array = np.loadtxt("data.txt", dtype=int) 
N = len(data_array)
#Charge_time = tmp[1]* 
#Discharge_time
# Chuyển đổi giá trị ADC thành Vôn và số lần đọc thành giây
voltage_array = data_array * tmp[0]
time_array = np.linspace(0, tmp[1]*(N-1), N)

# Thiết lập biểu đồ
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

# Đặt giá trị tối đa và tối thiểu cho thang đo
ax.set_xlim(0, 10)
ax.set_ylim(0, 3.5)

# Lưới
#ax.grid(True)
ax.grid(visible=None, which='major', axis='both', linestyle="-", linewidth=0.7, color='.50', zorder=-10)
ax.grid(visible=None, which='minor', axis='both', linestyle="--", linewidth=0.5, color='.50', zorder=-10)

# Nhãn trục, Tiêu đề
plt.ylabel("Напряжение, B")
plt.xlabel("Время, с")
plt.title("Процесс заряда и разряда конденсатора в RC-цепочке")

# Vẽ đường và điểm đánh dấu
ax.plot(time_array, voltage_array, 'o', ls='-', linewidth = 0.9, markersize = 6, markevery = 20, label=r"$V(t) = \varepsilon \cdot (1 - e^\frac{-t}{RC})$", c='b', mew = 1)

# Chú giải
ax.legend()

# Tự động xác định địa điểm của các dấu vạch trên trục x và y
ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_major_locator(ticker.AutoLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

ax.text(0.6, 0.62, "Время заряда = 4.21 с", fontsize=14, transform=ax.transAxes)
ax.text(0.6, 0.55, "Время разряда = 5.65 с", fontsize=14, transform=ax.transAxes)

# Lưu đồ thị vào file
plt.savefig('path/to/save/file.svg') 

plt.show()


