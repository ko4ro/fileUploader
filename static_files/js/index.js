// 参照ファイル名表示をJqueryで行う処理
$(document).on('change', ':file', function () {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.parent().parent().next(':text').val(label);
});

const LOAD_FILES_PAGE_SIZE = 10


// 以下　Vue.js
// ファイル一覧表示をJS側で行う処理
document.addEventListener("DOMContentLoaded", () => {
    let app = new Vue({
        delimiters: ["[[", "]]"],
        el: '#app', 
        data: {
            filenames: [],
        },
        methods: {
            validate_uploads:　function (event) {
                var file = event.target.files[0];
                name = file.name,
                size = file.size,
                type = file.type
                errors = ''
                
                console.log(file)

                //上限サイズは3MB
                if (size > 3000000) {
                  errors += 'ファイルの上限サイズ3MBを超えています\n'
                }
             
                //拡張子は .jpg .gif .png . pdf のみ許可
                if (type != 'image/jpeg' && type != 'image/png' && type != 'application/zip') {
                  errors += '.jpg、、.png、.zipのいずれかのファイルのみ許可されています\n'
                }
             
                if (errors) {
                  //errorsが存在する場合は内容をalert
                  alert(errors)
                  //valueを空にしてリセットする
                  event.currentTarget.value = ''
                }

                var reader = new FileReader();
                var preview = document.getElementById("preview");
                var previewImage = document.getElementById("previewImage");
                if(previewImage != null)
                    preview.removeChild(previewImage);

                reader.onload = function(event) {
                var img = document.createElement("img");
                img.setAttribute("src", reader.result);
                img.setAttribute("id", "previewImage");
                preview.appendChild(img);
            };
            reader.readAsDataURL(file);
        },
            loadfile: function (start = 0, size = 10) {
                self = this;
                let point = `http://localhost:8000/api/uploaded_files?start=${start}&size=${size}`
                fetch(point).then(function (response) {
                    return response.json();
                })
                    .then(function (myJson) {
                        self.filenames = self.filenames.concat(myJson.files);
                    });
            },
            loadFilesMore: function () {
                let start = this.filenames == null ? 0 : this.filenames.length
                this.loadfile(start, LOAD_FILES_PAGE_SIZE)
            },
            deleteItem: function(index){
                self = this;
                let target = `http://localhost:8000/api/delete?target=${self.filenames[index]}`
                fetch(target).then(function (response) {})
                if(confirm('Are you sure Delite?')){ //確認をとる
                // console.log(self.filenames[index]);
                self.filenames.splice(index, 1);
            }}
        }
    })
    app.loadfile();
    setTimeout(app.loadFilesMore, 1000)
})

