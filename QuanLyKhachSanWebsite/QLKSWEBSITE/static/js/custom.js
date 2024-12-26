document.addEventListener('DOMContentLoaded', () => {
    const guestInput = document.getElementById('guests');
    const guestDropdown = document.querySelector('.guest-dropdown');
    const applyButton = document.querySelector('.apply-btn');

    // Toggle dropdown visibility
    guestInput.addEventListener('click', () => {
        guestDropdown.style.display = guestDropdown.style.display === 'block' ? 'none' : 'block';
    });

    // Handle increase and decrease buttons
    document.querySelectorAll('.increase, .decrease').forEach(button => {
        button.addEventListener('click', (e) => {
            const target = e.target.getAttribute('data-target');
            const countSpan = document.getElementById(`${target}-count`);
            let currentValue = parseInt(countSpan.textContent, 10);

            if (e.target.classList.contains('increase')) {
                currentValue++;
            } else if (currentValue > 0) {
                currentValue--;
            }

            countSpan.textContent = currentValue;
        });
    });

    // Apply selected values
    applyButton.addEventListener('click', () => {
        const adults = document.getElementById('adults-count').textContent;

        guestInput.value = `${adults}`;
        guestDropdown.style.display = 'none';
    });

    // Close dropdown if clicked outside
    document.addEventListener('click', (e) => {
        if (!document.getElementById('guest-picker').contains(e.target)) {
            guestDropdown.style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const discountForm = document.getElementById('discount-form');
    const discountCodeInput = document.getElementById('discount-code');
    const discountMessage = document.getElementById('discount-message');

    const validCodes = {
        SALE20: 'Bạn đã áp dụng thành công giảm giá 20%!',
        FREESHIP: 'Bạn đã áp dụng thành công miễn phí vận chuyển!',
        TECH10: 'Bạn đã áp dụng thành công giảm giá 10% cho sản phẩm công nghệ!',
    };

    discountForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const code = discountCodeInput.value.trim().toUpperCase();

        if (validCodes[code]) {
            discountMessage.textContent = validCodes[code];
            discountMessage.classList.remove('hidden');
            discountMessage.style.color = 'green';
        } else {
            discountMessage.textContent = 'Mã giảm giá không hợp lệ. Vui lòng thử lại.';
            discountMessage.classList.remove('hidden');
            discountMessage.style.color = 'red';
        }

        discountCodeInput.value = '';
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const resultsTable = document.getElementById('results-table').getElementsByTagName('tbody')[0];
    const noResultsMessage = document.createElement('div'); // Tạo phần tử div cho thông báo

    noResultsMessage.classList.add('alert', 'alert-danger'); // Thêm lớp Bootstrap alert-danger
    noResultsMessage.style.display = 'none'; // Ẩn thông báo ban đầu

    noResultsMessage.textContent = 'Không có đơn hàng nào được tìm thấy'; // Nội dung thông báo

    const sampleOrders = [
        {id: 'ORD001', date: '2024-11-10', status: 'Đang xử lý', value: '500,000 VND'},
        {id: 'ORD002', date: '2024-11-12', status: 'Đã giao', value: '1,200,000 VND'},
        {id: 'ORD003', date: '2024-11-13', status: 'Đã hủy', value: '300,000 VND'},
        {id: 'ORD004', date: '2024-11-14', status: 'Đang xử lý', value: '700,000 VND'}
    ];

    // Hàm lọc đơn hàng theo thông tin nhập vào
    function filterOrders(orderId, orderDate) {
        return sampleOrders.filter(order => {
            const matchesId = orderId ? order.id.includes(orderId) : true;
            const matchesDate = orderDate ? order.date === orderDate : true;
            return matchesId && matchesDate;
        });
    }

    // Hàm hiển thị kết quả tìm kiếm lên bảng
    function displayResults(orders) {
        resultsTable.innerHTML = ''; // Xóa bảng trước khi hiển thị kết quả mới
        if (orders.length === 0) {
            resultsTable.parentElement.appendChild(noResultsMessage); // Thêm thông báo vào container
            noResultsMessage.style.display = 'block'; // Hiển thị thông báo
        } else {
            noResultsMessage.style.display = 'none'; // Ẩn thông báo
            orders.forEach(order => {
                const row = resultsTable.insertRow();
                row.insertCell(0).textContent = order.id;
                row.insertCell(1).textContent = order.date;
                row.insertCell(2).textContent = order.status;
                row.insertCell(3).textContent = order.value;
            });
        }
    }

    // Xử lý khi form tìm kiếm được gửi
    searchForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const orderId = document.getElementById('order-id').value.trim();
        const orderDate = document.getElementById('order-date').value.trim();


        const filteredOrders = filterOrders(orderId, orderDate);
        displayResults(filteredOrders);
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('container')
    const registerBtn = document.getElementById('register')
    const loginBtn = document.getElementById('login')

    registerBtn.addEventListener('click', () => {
        container.classList.add("active");
    })

    loginBtn.addEventListener('click', () => {
        container.classList.remove('active');
    })
});

document.addEventListener('DOMContentLoaded', () => {
    const promoTimer = document.getElementById('promo-timer');

    // Thời gian kết thúc khuyến mãi (tùy chỉnh thời gian)
    const promoEndTime = new Date();
    promoEndTime.setMinutes(promoEndTime.getMinutes() + 30); // Khuyến mãi kết thúc sau 30 phút

    // Hàm đếm ngược
    function updateTimer() {
        const now = new Date();
        const timeLeft = promoEndTime - now;

        if (timeLeft <= 0) {
            promoTimer.textContent = "Hết thời gian!";
            clearInterval(timerInterval);
            return;
        }

        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
        promoTimer.textContent = `${minutes} phút ${seconds} giây`;
    }

    // Cập nhật mỗi giây
    updateTimer();
    const timerInterval = setInterval(updateTimer, 1000);
});

let currentField;

function openPopup(field) {
    // Store the current field for later use
    currentField = field;

    // Reset the form inputs
    document.getElementById('popupForm').reset();

    // Open the modal
    const modal = new bootstrap.Modal(document.getElementById('inputModal'));
    modal.show();
}

function saveData() {
    // Get the values from the form inputs
    const fullName = document.getElementById('fullName').value.trim();
    const identityCard = document.getElementById('identityCard').value.trim();
    const loaiKhach = document.getElementById('loaiKhach').value;

    // Validate inputs
    if (fullName && identityCard && loaiKhach) {
        // Update the label of the current field
        const targetLabel = document.getElementById(`label${currentField}`);
        if (targetLabel) {
            targetLabel.innerText = `${fullName} (${identityCard}) - ${loaiKhach}`;
        }

        // Close the modal
        const modal = bootstrap.Modal.getInstance(document.getElementById('inputModal'));
        if (modal) {
            modal.hide();
        }
    } else {
        alert('Vui lòng nhập đầy đủ thông tin!');
    }
}

function deleteCustomer(field) {
    const label = document.getElementById(`label${field}`);
    if (label) {
        label.innerText = `Khách hàng ${field}`; // Reset the label text
        alert(`Đã xóa thông tin của Khách hàng ${field}`); // Optionally, show a message
    }
}

function updateMaxCustomers(luongKhachToiDa) {
    // Tính số phòng được chọn
    const selectedRooms = document.querySelectorAll('.form-check-input:checked').length;

    // Lấy giới hạn khách tối đa trên mỗi phòng
    const maxCustomersPerRoom = luongKhachToiDa;

    // Tính tổng số khách tối đa
    const maxCustomers = selectedRooms * maxCustomersPerRoom;

    // Hiện hoặc xóa bớt khách hàng nếu cần
    const customerList = document.querySelectorAll('[id^="label"]');
    if (customerList.length > maxCustomers) {
        for (let i = customerList.length; i > maxCustomers; i--) {
            deleteHTMLCustomer(i); // Gọi hàm xóa khách hàng
        }
    }
    return maxCustomers
}

document.querySelectorAll('.form-check-input').forEach(input => {
    input.addEventListener('change', () => {
        updateMaxCustomers();
    });
});

function deleteHTMLCustomer(field) {
    const label = document.getElementById(`label${field}`);
    if (label) {
        label.parentElement.remove(); // Xóa toàn bộ phần tử li của khách hàng
    }
}


function addCustomer(luongKhachToiDa) {
    const customerList = document.querySelectorAll('[id^="label"]');
    const maxCustomers = updateMaxCustomers(luongKhachToiDa); // Gọi lại hàm để tính giới hạn

    if (customerList.length < maxCustomers) {
        const newCustomerIndex = customerList.length + 1;

        const newCustomerItem = document.createElement('li');
        newCustomerItem.className = 'mb-3 d-flex align-items-center justify-content-between';
        newCustomerItem.innerHTML = `
        <span id="label${newCustomerIndex}">Khách hàng ${newCustomerIndex}</span>
        <div>
        <button class="btn btn-outline-primary btn-sm" onclick="openPopup(${newCustomerIndex})">Nhập Thông Tin</button>
        <button class="btn btn-outline-danger btn-sm ms-2" onclick="deleteCustomer(${newCustomerIndex})">Xóa</button>
        </div>
        `;

        document.querySelector('.list-unstyled').appendChild(newCustomerItem);
    } else {
        alert('Không thể thêm khách hàng vượt quá số lượng tối đa!');
    }
}


function submitForm() {
    document.getElementById('formLoaiPhong').submit(); // Tự động gửi form
}

function collectFormData() {
    // Lấy giá trị từ dropdown idLoaiPhong
    const idLoaiPhong = document.querySelector('[name="idLoaiPhong"]').value;
    document.getElementById('hiddenIdLoaiPhong').value = idLoaiPhong;

    // Lấy giá trị từ input datetime-local ngayTraPhong
    const ngayTraPhong = document.querySelector('[name="ngayTraPhong"]').value;
    document.getElementById('hiddenNgayTraPhong').value = ngayTraPhong;

    // Lấy danh sách phòng được chọn
    const phongDuocChon = Array.from(document.querySelectorAll('.form-check-input:checked'))
        .map(input => input.nextElementSibling.innerText.trim())
        .join(', ');
    document.getElementById('hiddenPhongDuocChon').value = phongDuocChon;

    // Lấy danh sách khách hàng
    const khachHang = Array.from(document.querySelectorAll('[id^="label"]'))
        .map(label => label.innerText.trim())
        .filter(text => !text.startsWith('Khách hàng ')) // Loại bỏ các khách hàng chưa được nhập thông tin
        .join('; ');
    document.getElementById('hiddenKhachHang').value = khachHang;
}

function submitMainForm() {
    if (validateForm()) {
        collectFormData(); // Thu thập dữ liệu trước khi submit
        document.getElementById('mainForm').submit();
    }
}

function validateForm() {
    // Kiểm tra dropdown idLoaiPhong
    const idLoaiPhong = document.querySelector('[name="idLoaiPhong"]').value;
    if (!idLoaiPhong) {
        alert('Vui lòng chọn loại phòng.');
        return false;
    }

    // Kiểm tra input datetime-local ngayTraPhong
    const ngayTraPhong = document.querySelector('[name="ngayTraPhong"]').value;
    if (!ngayTraPhong) {
        alert('Vui lòng chọn ngày trả phòng.');
        return false;
    }

    // Kiểm tra ít nhất một phòng được chọn
    const phongDuocChon = document.querySelectorAll('.form-check-input:checked');
    if (phongDuocChon.length === 0) {
        alert('Vui lòng chọn ít nhất một phòng.');
        return false;
    }

    // Kiểm tra ít nhất một khách hàng đã được nhập thông tin
    const khachHang = Array.from(document.querySelectorAll('[id^="label"]'))
        .some(label => !label.innerText.startsWith('Khách hàng '));
    if (!khachHang) {
        alert('Vui lòng nhập thông tin cho ít nhất một khách hàng.');
        return false;
    }

    return true; // Tất cả đều hợp lệ
}


