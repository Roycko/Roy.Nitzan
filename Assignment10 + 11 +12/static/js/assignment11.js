console.log("Im in");

function getUsers(){
    console.log("yaaaaaa");
    fetch('https://reqres.in/api/users').then(
        response => response.json()
    ).then(
        responseObj => users_in_html(responseObj.data)
    ).catch(
        err => console.log(err)
    )
}


function users_in_html(response_obj){
    // console.log(response_obj);
    const curr_main = document.querySelector("main");
    for (let user of response_obj){
        const usersSection = document.createElement('usersSection')
        usersSection.innerHTML =`
            <img src="${user.avatar}" alt="Picture"/>
            <div>
                <span>${user.first_name} ${user.last_name}</span>
                <br>
                <a href="mailto:${user.email}"> Send Email</a>
            </div>
        `;
        curr_main.appendChild(usersSection)
    }

}