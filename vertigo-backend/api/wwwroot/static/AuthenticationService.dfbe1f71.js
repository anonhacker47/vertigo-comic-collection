import{A as r}from"./index.a4ef9cc4.js";const n={register(e){return r().post("users",e)},login(e){return r().post("tokens",null,e)},refreshToken(e){return r().put("tokens",e)}};export{n as A};
