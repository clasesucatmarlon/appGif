(this["webpackJsonpproj-gif-expert-app"]=this["webpackJsonpproj-gif-expert-app"]||[]).push([[0],{17:function(t,e,n){},18:function(t,e,n){"use strict";n.r(e);var a=n(0),c=n(1),r=n(7),i=n.n(r),s=n(2),u=n(9),o=function(t){var e=t.setCateg,n=Object(c.useState)(""),r=Object(s.a)(n,2),i=r[0],o=r[1];return Object(a.jsx)("form",{onSubmit:function(t){t.preventDefault(),i.trim().length>2&&(e((function(t){return[i].concat(Object(u.a)(t))})),o(""))},children:Object(a.jsx)("input",{type:"text",value:i,onChange:function(t){o(t.target.value)}})})},j=n(10),d=function(t){var e=t.id,n=t.title,c=t.url;return console.log({id:e,title:n,url:c}),Object(a.jsxs)("div",{className:"card animate__animated animate__flip",children:[Object(a.jsx)("img",{src:c,alt:n}),Object(a.jsx)("p",{children:n})]})},l=n(6),p=n.n(l),f=n(8),m=function(){var t=Object(f.a)(p.a.mark((function t(e){var n,a,c,r,i;return p.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return n="https://api.giphy.com/v1/gifs/search?q=".concat(encodeURI(e),"&limit=10&api_key=pOFtYHGzH718DYtBKguubBLqSqEdL6IS"),t.next=3,fetch(n);case 3:return a=t.sent,t.next=6,a.json();case 6:return c=t.sent,r=c.data,i=r.map((function(t){var e;return{id:t.id,title:t.title,url:null===(e=t.images)||void 0===e?void 0:e.downsized_medium.url}})),t.abrupt("return",i);case 10:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),b=function(t){var e=t.category,n=function(t){var e=Object(c.useState)({data:[],loading:!0}),n=Object(s.a)(e,2),a=n[0],r=n[1];return Object(c.useEffect)((function(){m(t).then((function(t){setTimeout((function(){r({data:t,loading:!1})}),3e3)}))}),[t]),a}(e),r=n.data,i=n.loading;return Object(a.jsxs)(a.Fragment,{children:[i&&Object(a.jsx)("p",{className:"animate__animated animate__flash animate__delay-3s",children:"Cargando informaci\xf3n ..."}),Object(a.jsx)("div",{className:"title",children:Object(a.jsx)("h3",{className:"animate__animated animate__fadeInDownBig",children:e})}),Object(a.jsx)("div",{className:"card-grid",children:r.map((function(t){return Object(a.jsx)(d,Object(j.a)({},t),t.id)}))})]})},O=function(){var t=Object(c.useState)(["dogs"]),e=Object(s.a)(t,2),n=e[0],r=e[1];return Object(a.jsxs)(a.Fragment,{children:[Object(a.jsx)("h2",{children:"GifExpertApp"}),Object(a.jsx)(o,{setCateg:r}),Object(a.jsx)("hr",{}),n.map((function(t){return Object(a.jsx)(b,{category:t},t)}))]})};n(17);i.a.render(Object(a.jsx)(O,{}),document.getElementById("root"))}},[[18,1,2]]]);
//# sourceMappingURL=main.1b62210f.chunk.js.map