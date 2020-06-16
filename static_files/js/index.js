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
            loadfile: function (start = 0, size = 10) {
                self = this;
                let point = `http://localhost:8000/api/uploaded_files?start=${start}&size=${size}`
                fetch(point).then(function (response) {

                    return response.json();
                })
                    .then(function (myJson) {
                        self.filenames = self.filenames.concat(myJson.files);
                        // console.log(self.filenames);
                        // console.log(myJson);

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

