Vue.use(BootstrapVue);

const DishesSummaryTemplate = `
<div class="p-5">
    <h1>Вы выбрали:</h1>
    <div class="row p-5">
        <div
        v-if="dishes"
        v-for="dish in dishes"
        class="col-md-4 pt-5"
        >
            <h4>{{ dish.name }}</h4>
            <p>Цена: {{ dish.price }} рублей</p>
            <p>Белки: {{ dish.nutritional_value.proteins }} на 100гр.</p>
            <p>Жиры: {{ dish.nutritional_value.fats }} на 100гр.</p>
            <p>Углеводы: {{ dish.nutritional_value.carbohydrates }} на 100гр.</p>
            <p>Калории: {{ dish.nutritional_value.calories }} Кал.</p>
            <img
                :src="get_dish_picture_url(dish)"
                class="mw-100 mh-300"
            />
        </div>
    </div>
    <h2 class="table-bordered mt-5 mb-2">Аллергены 😱:</h2>
    <p v-for="allergen in allergens">
        {{ allergen }}
    </p>
    <h2 class="table-bordered mt-5 mb-2">Итого: {{total_price()}} рублей.</h2>
</div>
`;


app = new Vue({
    el: '#dishes_summary_app',
    data: {
        dishes: [],
        allergens: [],
    },
    template: DishesSummaryTemplate,
    methods: {
        /**
         * Prepare dish picture url
         */
        get_dish_picture_url: function (dish) {
            if (dish.picture) {
                return dish.picture.picture;
            } else {
                return "https://www.python.org/static/community_logos/python-powered-h-50x65.png";
            }
        },
        /**
         * Calculate price of all checked dishes
         * @returns {number}
         */
        total_price: function () {
            var price = 0;
            for (dish of this.dishes) {
                price += dish.price;
            }
            return price;
        },
    },
    mounted: function () {
        var that = this;
        // Get checked dishes from cookie and make dished ids string for API request
        var checked_dishes = $cookies.get('checked_dishes');
        var dishes_ids = "";
        for (dish_id of Object.keys(checked_dishes)) {
            if (checked_dishes[dish_id] == true){
                dishes_ids += `${dish_id},`;
            }
        }
        // Make API request with dishes ids GET param
        axios.get(`${API_URLS.dishes}?dishes=${dishes_ids}`)
            .then((response) => {
                that.dishes = response.data;
                that.allergens = [];
                // Collect allergens from all checked dishes
                for (dish of that.dishes) {
                    for (allergen of dish.allergens) {
                        if (!that.allergens.includes(allergen.name)) {
                            that.allergens.push(allergen.name);
                        }
                    }
                }
            });
    },



});
