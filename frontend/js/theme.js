class Theme {
   constructor(bgColor, textColor) {
     this.bgColor = bgColor;
     this.textColor = textColor;
   }

   apply() {
     // Método para aplicar o tema
      document.body.style.backgroundColor = this.bgColor;
      document.body.style.color = this.textColor;
      document.getElementById("container-params").style.color = this.textColor;
      document.getElementById("container-params").style.backgroundColor = this.bgColor;
      const elementsDiv = document.querySelectorAll("span");
      elementsDiv.forEach(td => {
         td.style.color = this.textColor;
      });
      const elements = document.querySelectorAll("td");
      elements.forEach(td => {
         td.style.color = this.textColor;
      });
      const elementsTh = document.querySelectorAll("th");
      elementsTh.forEach(td => {
         td.style.color = this.textColor;
      });
      const elementsInput = document.querySelectorAll("input");
      elementsInput.forEach(td => {
         td.style.color = this.textColor;
         td.style.backgroundColor = this.bgColor;
      });
      const elementsSelect = document.querySelectorAll("select");
      elementsSelect.forEach(td => {
         td.style.color = this.textColor;
         td.style.backgroundColor = this.bgColor;
      });
   }
 }

 // Subclasse para tema claro
 class LightTheme extends Theme {
   constructor() {
     super('#ffffff', '#000000');
   }
 }

 // Subclasse para tema escuro
 class DarkTheme extends Theme {
   constructor() {
     super('#333333', '#ffffff');
   }
 }

 function changeTheme(theme) {
   theme.apply();
 }

 const lightTheme = new LightTheme();
 const darkTheme = new DarkTheme();

 // Mudar para tema claro
 document.getElementById('changeThemeButton').addEventListener('click', function() {
   changeTheme(lightTheme);
   console.log('click theme');
 });

 // Mudar para tema escuro
 document.getElementById('changeThemeButton').addEventListener('contextmenu', function(event) {
   event.preventDefault(); // Impedir o menu de contexto padrão
   console.log('click theme');
   changeTheme(darkTheme);
 });