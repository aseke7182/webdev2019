var cnt = 1;
var q = -1;
start();

function buttonClick(){
    var text = document.getElementById("userInput").value;
    document.getElementById("userInput").value = "";
    if(text.length > 0) {
        //first div
        var row = document.getElementById("row");
        var task = document.createElement("div");
        row.appendChild(task);
        task.className = "task";
        task.id = cnt;

        //chechbox
        var checkbox = document.createElement("input");
        var checkBoxDiv = document.createElement("div");
        checkbox.className = "checkbox";
        task.appendChild(checkBoxDiv);
        checkBoxDiv.appendChild(checkbox);
        checkbox.type = "checkbox";
        checkbox.onclick = function Do(){
            var par = this.parentElement.parentElement.getElementsByClassName('texts')[0].firstChild;
            if(this.checked){
                par.className = "no";
            }else{
                par.className = "yes";
            }
        }

        //our task
        var paragraphDiv = document.createElement("div");
        paragraphDiv.className = "texts";
        var paragraph = document.createElement("p");
        paragraph.className = cnt;
        task.appendChild(paragraphDiv);
        paragraphDiv.appendChild(paragraph);
        paragraph.innerHTML = text;
        paragraph.className = "yes";

        //delete button
        var deleteDiv = document.createElement("div");
        var deletes = document.createElement("button");
        deletes.className = "del";
        deletes.innerHTML = "delete";
        task.appendChild(deleteDiv);
        deleteDiv.appendChild(deletes);
        deletes.onclick = function go(){
            this.parentElement.parentElement.remove();
        }
        cnt++;
    }else{
        alert("At Least One Element");
    }
 }

 function start(){
    Timer();
    Alive();
    setInterval(Timer,1000);
    setInterval(Alive,1000*60);
 } 
function Alive(){
    q++;
    let a = document.getElementById("ha");
    if(q==0 || q==1){
        a.innerHTML = `${q} Minute`;
    }else{
        a.innerHTML = `${q} Minutes`;
    }
}

function Die(){
    let b = Math.floor(Math.random()*20);
    // create array of murphy laws
    let ar = new Array(20)
    ar[0] = "Nothing is as easy as it looks."
    ar[1] = "Everything takes longer than you think."
    ar[2] = "Anything that can go wrong will go wrong."
    ar[3] = "If there is a possibility of several things going wrong, the one that will cause the most damage will be the one to go wrong."
    ar[4] = "If there is a worse time for something to go wrong, it will happen then."
    ar[5] = "If anything simply cannot go wrong, it will anyway."
    ar[6] = "Just Code It."
    ar[7] = "Left to themselves, things tend to go from bad to worse."
    ar[8] = "If everything seems to be going well, you have obviously overlooked something."
    ar[9] = "Nature always sides with the hidden flaw."
    ar[10] = "Just Do It."
    ar[11] = "It is impossible to make anything foolproof because fools are so ingenious."
    ar[12] = "Whenever you set out to do something, something else must be done first."
    ar[13] = "Every solution breeds new problems."
    ar[14] = "Trust everybody ... then cut the cards."
    ar[15] = "Two wrongs are only the beginning."
    ar[16] = "If at first you don't succeed, destroy all evidence that you tried."
    ar[17] = "To succeed in politics, it is often necessary to rise above your principles."
    ar[18] = "Exceptions prove the rule ... and wreck the budget."
    ar[19] = "Success always occurs in private, and failure in full view."
    let here = document.getElementById("die");
    let wow  = document.getElementById("maybe");
    wow.innerHTML = "Click On Me And ... Get Random Quote : ";
    here.innerHTML = `${ar[b]}`;
}

 function Timer(){
    var now = new Date();
    var min = now.getMinutes();
    var sec = now.getSeconds();
    let hours = now.getHours();
    let mo = now.getMonth();
    if(mo == 1){
        mo = "February";
    }
    console.log(mo);
    const year = now.getFullYear();
    let p = document.getElementById("time");
    let c = document.getElementById("year");
    p.innerHTML = `${hours}:${min}:${sec}`;
    c.innerHTML = `${year} ${mo}`;
 }