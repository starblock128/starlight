//滑鼠區塊
    let intervalId = null; //設定intervalId全域變數，儲存一個計時函示setInterval()的ID，方便後續停止

    //重複發送action的機制，用於長按按鈕時重複執行
    function startSend(action) {
        if (intervalId) return; //先確認現在有沒有計時函示在執行，避免重複
        send(action); //先執行一次，後會會等delay時間後再重複執行
        
        //setInterval()JS的計時函示，會每隔指定的毫秒數執行一次指定的函式，setInterval(function, delay)
        //() => send(action)，JS箭頭函式簡化寫法，等於是指定function()內容
        intervalId = setInterval(() => send(action), 100);
    }

    //停止計時函示setInterval()
    function stopSend() {
        clearInterval(intervalId); //clearInterval()，JS內建函式，用來停止 setInterval()所建立的計時器
        intervalId = null;
    }

    //發送 action 到後端，action的值來自於呼叫send()的地方，例如按鈕事件
    function send(action) {
        fetch('/api/mouse', { //發送到後端的/api/mouse(API endpoint一個URL路徑地址)
            method: 'POST', //使用POST方法，代表輸出資料
            headers: {'Content-Type': 'application/json'}, //請求內容型態是Content-Type，內容是application/json(JSON 格式)
            body: JSON.stringify({hid_action: action}) //用JSON.stringify把 {action: action} JS物件轉成 JSON 字串
        });
    }

    //偵測到按鈕按下時，執行startSend()，直到放開或中斷後執行stopSend()
    function bindButton(id, action) { //id 按鈕識別參數 action 該按鈕對應的動作參數
        const btn = document.getElementById(id); //用id找到對應的HTML按鈕元素，並存到btn
        
        //.addEventListener是JS的DOM API，用來在HTML元素上註冊事件監聽器（事件處理函式），當該事件發生時，執行指定的函式
        //用法 element.addEventListener(eventType 要偵測的事件, listener 要執行的函式)
        btn.addEventListener('pointerdown', (e) => { //pointerdown 瀏覽器內建的事件類型(Pointer Events API)，滑鼠或觸控按下
            e.preventDefault(); //防止瀏覽器預設行為（例如長按選字、拖曳），JS事件物件的方法
            startSend(action); //前面設定的重複執行函式
        });

        //設定什麼情況下執行stopSend()，停止setInterval()
        btn.addEventListener('pointerup', stopSend); //手指或滑鼠放開
        btn.addEventListener('pointercancel', stopSend);//觸控操作被瀏覽器中斷時
        btn.addEventListener('pointerleave', stopSend);//手指或滑鼠離開按鈕區域
        window.addEventListener('pointerup', stopSend);//全域監聽預防性措施
    }

    //綁定按鈕的動作，發出action指令up,down,left,right
    bindButton('btn-up', 'up');
    bindButton('btn-down', 'down');
    bindButton('btn-left', 'left');
    bindButton('btn-right', 'right');