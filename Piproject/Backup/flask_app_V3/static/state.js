//資訊顯示
    //顯示現在日期時間
    function updateTime() {
        const now = new Date();
        const options = { 
            year: 'numeric', 
            month: '2-digit', 
            day: '2-digit', 
            hour: '2-digit', 
            minute: '2-digit', 
            second: '2-digit' 
        };
        document.getElementById('currentTime').textContent = now.toLocaleString('zh-TW', options);
    }

    setInterval(updateTime, 1000); // 每秒更新一次
    updateTime(); // 初始化