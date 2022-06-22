

function loading(){
    const accdb_path = document.getElementById("access path").value;
    const bernc_path = document.getElementById("bernc path").value;
    const dicc_path = document.getElementById("dicc path").value;
    const dec_l_m_path = document.getElementById("dec last month path").value;
    console.log(accdb_path)
    if((accdb_path!='')&&(bernc_path!='')&&(dicc_path!='')&&(dec_l_m_path!='')){
        document.getElementById("loading").style.display = 'flex';
        document.getElementById("content").style.display = 'none';
    }
}