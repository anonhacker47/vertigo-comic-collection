import{r as s,b as d,o as n,d as i,e,w as l,P as m,t as p,f as u,g as _,A as f}from"./index.a61c5230.js";const g={class:"flex justify-center items-center h-screen"},y=_("h1",{class:"text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"}," Create your Vertigo Account ",-1),w={key:0,class:"error py-5"},v={__name:"SignupView",setup(h){s(""),s(""),s("");const t=s("");async function c(r){try{const o=await f.register({username:r.username,email:r.email,password:r.password})}catch(o){t.value=o.response.data.errors}console.log(t)}return(r,o)=>{const a=d("FormKit");return n(),i("div",g,[e(m,null,{default:l(()=>[y,e(a,{type:"form","submit-label":"Sign up",onSubmit:c},{default:l(()=>[e(a,{type:"text",name:"username",label:"Username",validation:"required"}),e(a,{type:"email",name:"email",label:"Email Address",validation:"required|email|",placeholder:"demo@company.com"}),e(a,{type:"password",name:"password",label:"Password",validation:"required"}),e(a,{type:"password",name:"password_confirm",label:"Confirm Password",validation:"required|confirm","validation-label":"Password confirmation"}),t.value!=""?(n(),i("h1",w,p(t.value),1)):u("",!0)]),_:1})]),_:1})])}}};export{v as default};
