//鍵盤區塊
    //輸出輸入框內的文字
    function sendText() {
        const str_text = document.getElementById('inputText').value; //讀取輸入框內的文字到text
        if (!str_text) return; //如果是空的就終止
        fetch('/api/keyboard', { //發送到後端的/api/keyboard
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({hid_text: str_text}) //用hid_text:判斷這是文字輸入
        }).then(() => { //.then非同步，請求完成後執行這段程式
            document.getElementById('inputText').value = ''; //清空輸入框
        });
    }

    //按下功能鍵
    function sendKey(keyName) {
        fetch('/api/keyboard', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ hid_key: keyName }) //hid_key:判斷這是按下功能鍵
        });
    }
