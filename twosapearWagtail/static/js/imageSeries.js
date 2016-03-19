var Series = Series || 
    function (imgId,images)
    {
        this.img = document.getElementById(imgId);
        this.x = -1;
        this.images = images;
        this.displayNextImage = function ()
        {
            this.x = (this.x === this.images.length - 1) ? 0 : this.x + 1;
            this.img.src = this.images[this.x];
        };
        this.displayImage = function (x)
        {
            this.img.src = this.images[x];
        };
        this.displayNextImage();
    };