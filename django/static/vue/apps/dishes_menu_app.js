Vue.use(BootstrapVue);

const DishesMenuTemplate = `
<div>
    <b-button 
        class="fixed-top pt-3 pb-3 submit-button" 
        :href="pastebin_url()"
        target="_blank"
    >
        Импортни нас на PasteBin!
    </b-button>
    <div class="pt-5 pb-5"></div>
    <h1>Меню:</h1>
    <div
    v-if="categoried_dishes"
    v-for="category in categoried_dishes"
    >
        <h2 class="mt-5 table-bordered">{{ category.name }}</h2>
        <div class="row p-5">
            <div
                v-for="dish in category.dishes"
                class="col-md-4 pt-5"
            >
                <h4>{{ dish.name }}</h4>
                <p>Цена: {{ dish.price }} рублей</p>
                <p>Белки: {{ dish.nutritional_value.proteins }} на 100гр.</p>
                <p>Жиры: {{ dish.nutritional_value.fats }} на 100гр.</p>
                <p>Углеводы: {{ dish.nutritional_value.carbohydrates }} на 100гр.</p>
                <p>Калории: {{ dish.nutritional_value.calories }} Кал.</p>
                <p>Аллергены: {{ get_allergens_string(dish) }}</p>
                <b-form-checkbox
                  v-model="checked_dishes[dish.id]"
                  @input="save_checked_dishes"
                  size="lg"
                >
                    Выбрать
                </b-form-checkbox>
                <img
                    :src="get_dish_picture_url(dish)"
                    class="mw-100 mh-300"
                />
            </div>
        </div>
    </div>
    <b-button class="fixed-bottom pt-3 pb-3 submit-button" :href="summary_url()">Отправить</b-button>
    <div class="pt-5 pb-5"></div>
    
</div>
`;


app = new Vue({
    el: '#dishes_menu_app',
    data: {
        categoried_dishes: {},
        checked_dishes: {},
    },
    template: DishesMenuTemplate,
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
         * Prepare allergens string for dish object
         * @param dish
         * @returns {string}
         */
        get_allergens_string: function (dish) {
            var allergens = [];
            for (allergen of dish.allergens) {
                allergens.push(allergen.name);
            }
            return allergens.join(', ');
        },
        /**
         * Save checked dishes to cookie
         */
        save_checked_dishes: function () {
            $cookies.set('checked_dishes', JSON.stringify(this.checked_dishes));
        },
        /**
         * Summary page url
         * @returns {string}
         */
        summary_url: function () {
            return URLS.summary;
        },
        /**
         * Last PasteBin paste url
         * @returns {string}
         */
        pastebin_url: function () {
            return URLS.pastebin;
        },
    },
    mounted: function () {
        var that = this;
        // Make api request to getting all dishes
        axios.get(API_URLS.dishes)
            .then((response) => {
                // Mapping dishes by categories
                var categoried_dishes = {};
                response.data.map(function(dish){
                    if (categoried_dishes[dish.category.id] == undefined){
                        categoried_dishes[dish.category.id] = {dishes: [], name: dish.category.name};
                    }
                    categoried_dishes[dish.category.id].dishes.push(dish);
                    that.checked_dishes[dish.id] = false;
                });
                that.categoried_dishes = categoried_dishes;
                that.save_checked_dishes(); // Save checked dished to cookie
            });
    },
});
