function showNotification(text) {
    const box = document.createElement("div");

    box.innerHTML = text;
    box.style.position = "fixed";
    box.style.top = "20px";
    box.style.right = "20px";

    box.style.background = "#2563eb";
    box.style.color = "white";
    box.style.padding = "15px 20px";
    box.style.borderRadius = "10px";
    box.style.boxShadow = "0 10px 25px rgba(0,0,0,.2)";
    box.style.zIndex = "9999";
    box.style.fontFamily = "system-ui";

    document.body.appendChild(box);

    setTimeout(() => {
        box.remove();
    }, 6000);
}


async function checkReminders() {
    try {
        const res = await fetch("/api/reminders/check");
        
        const data = await res.json();

        data.forEach(r => {
            showNotification(
                `⏰ Zadanie ${r.task_id}<br>
                 Przypomnienie o ${new Date(r.notify_at).toLocaleTimeString()}`
            );
        });

    } catch (e) {
        console.error("Reminder error", e);
    }
}


setInterval(checkReminders, 60000);

checkReminders();
