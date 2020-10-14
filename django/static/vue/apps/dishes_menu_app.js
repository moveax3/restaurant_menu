Vue.use(BootstrapVue);

const DishesMenuTemplate = `
<div>
    <h1>Меню:</h1>
    <div
    v-if="categoried_dishes"
    v-for="category in categoried_dishes"
    >
        <h2 class="mt-5 table-bordered">{{ category.name }}</h2>
        <div class="row p-5">
            <div
                v-for="dish in category.dishes"
                class="col-md-4"
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
                    :src="dish.picture.picture"
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
        get_allergens_string: function (dish) {
            var allergens = [];
            for (allergen of dish.allergens) {
                allergens.push(allergen.name);
            }
            return allergens.join(', ');
        },
        save_checked_dishes: function () {
            $cookies.set('checked_dishes', JSON.stringify(this.checked_dishes));
        },
        summary_url: function () {
            return URLS.summary;
        }
    },
    mounted: function () {
        var that = this;
        axios.get(API_URLS.dishes)
            .then((response) => {
                var categoried_dishes = {};
                response.data.map(function(dish){
                    if (categoried_dishes[dish.category.id] == undefined){
                        categoried_dishes[dish.category.id] = {dishes: [], name: dish.category.name};
                    }
                    categoried_dishes[dish.category.id].dishes.push(dish);
                    that.checked_dishes[dish.id] = false;
                });
                that.categoried_dishes = categoried_dishes;
                that.save_checked_dishes();
            });
    },
});